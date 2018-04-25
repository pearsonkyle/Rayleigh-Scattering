import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import minimize

kb = 1.38064852e-23 # m2 kg s-2 K-1



# model fit function
def sigma_ray(x,*args):
    # cross section of h2 (cm2), x=wavelength(A)
    return  np.vstack( [ args[i]/x**(4+2*i) for i in range(len(args))] ).sum(0)

def sigma_ray2(x,*args):
    # cross section of h2 (cm2), x=wavelength(A)
    return  np.vstack( [ args[i]/(args[i+1]+x**(4+2*i)) for i in range(0,len(args),2)] ).sum(0)



def polarizability(N,m):
    # polarizability from Lorentz-Lorenz Formula
    # N - number density
    # m - index of refraction (n-ik)
    #  various approximations below

    #return (m**2 -1)/(4*np.pi*N)
    #return (m-1)/(2*np.pi*N)
    return 3*(m**2-1) / (4*np.pi*N*(m**2+2))

def ray(l,a,d):
    # analytic expression for rayleigh scattering (Goody & Yung 1989)
    # compute anistropy of molecule/atom with d (depolarization factor)
    # l, wavelength (m)
    # a, polarizability

    fani = (6+3*d)/(6-7*d)
    return  fani * 128*np.pi**5 * a**2 / (3*l**4)

def fn2min(pars, *args):
    #  *ARGS [xdata, ydata, cost_fn, model_fn]
    model = args[-1](args[0], *pars)
    cost = args[2](args[1],model).sum()
    return cost

# interpolate data to a new set of points
interp1d = lambda x,y,xnew : interpolate.interp1d(x,y,kind='linear', bounds_error=False, fill_value="extrapolate")(xnew)

# cost functions
chisqr = lambda d,m : np.abs(m-d)#**2  # chi square
errorp = lambda d,m : np.abs(d-m)/d  # percent difference sum from data

if __name__ == "__main__":

    # H2 cross section from Shardanand 1977
    x,y = np.loadtxt('n2rayleigh.dat').T

    # compute cross section with refraction measurements per wavelength
    frac = np.loadtxt('n2refraction.txt')
    a = polarizability(101325/(kb*273), frac[:,1] )
    cross = ray(frac[:,0]*1e-6,a, 0.03)*1e4 # m2*1e4 -> cm2
    res = minimize(fn2min,x0=[5e-12,0,0],method='Nelder-Mead',args=(frac[:,0]*1e4,cross,errorp,sigma_ray) )
    frac_c = sigma_ray(x,*res.x)
    #frac_c = interp1d(frac[:,0]*1e4, cross, x) # interpolate to same grid as H2 cs data

    # fit some models to the data
    names = ['ChiSqr (3)', '% Error (3)','ChiSqr (1)','% Error (1)']
    inits = [[8.14e-13,1.28e-6,1.61]]*2 + [[5e-12]]*2
    modes = [ (chisqr,sigma_ray), (errorp,sigma_ray),(chisqr,sigma_ray), (errorp,sigma_ray)]
    res = [ minimize(fn2min,x0=inits[i],method='Nelder-Mead',args=(x,y,*modes[i])) for i in range(len(modes)) ]
    ydata = [ modes[i][1](x,*res[i].x) for i in range(len(modes)) ]


    f,ax = plt.subplots(2,2,figsize=(11, 6))
    plt.subplots_adjust(left=0.1, right=0.97, bottom=0.09, top=0.88,hspace=0.11,wspace=0.24)
    for i in range(len(ydata)):
        ax[0,0].plot(x, np.log10(ydata[i]), label=names[i])

        ax[1,0].plot(x, np.log10(chisqr(y, modes[i][1](x,*res[i].x))), label="{:.2E}".format(chisqr(y, modes[i][1](x,*res[i].x)).sum() ) )
        #ax[1,0].plot(x, np.log10(y)-np.log10(modes[i][1](x,*res[i].x)), label="{:.2E}".format(chisqr(y, modes[i][1](x,*res[i].x)).sum() ) )

        ax[1,1].plot(x, 1-modes[i][1](x,*res[i].x)/y, label="{:.2f}".format( np.abs(1-modes[i][1](x,*res[i].x)/y).sum()  ))
        #ax[1,1].plot(x, errorp(y, modes[i][1](x,*res[i].x)), label=names[i])



    ax[0,0].plot(x,np.log10(frac_c),label='Refraction')
    ax[1,0].plot(x,np.log10(chisqr(y, frac_c)), label="{:.2E}".format(chisqr(y, frac_c).sum() ) )
    #ax[1,0].plot(x,np.log10(y)-np.log10(frac_c), label="{:.2E}".format(chisqr(y, frac_c).sum() ) )
    ax[1,1].plot(x, 1-frac_c/y, label="{:.2f}".format( np.abs(1-frac_c/y).sum()  ))

    ax[0,0].plot(x,np.log10(y),'k.',label='Data')
    ax[0,0].legend(loc='best')
    ax[1,0].legend(loc='best')
    ax[1,1].legend(loc='best')
    ax[1,0].set_xlabel('Wavelength (A)')
    ax[0,0].set_ylabel('Log10( Cross Section [cm2] )')
    ax[1,0].set_ylabel('Log10( |Data-Model| )')
    ax[1,1].set_ylabel('Percent Error')
    ax[1,1].set_xlabel('Wavelength (A)')


    ax[1,1].grid(True)
    ax[0,1].axis('tight')
    ax[0,1].axis('off')
    ax[0,1].text(-0.05, 0.025, r'$\frac{%0.2e}{\lambda^{4}}$+$\frac{%0.2e}{\lambda^{6}}$+$\frac{%0.2f}{\lambda^{8}}$' %(res[1].x[0],res[1].x[1],res[1].x[2]), style='italic',fontsize=16,
        bbox={'facecolor':'orange', 'alpha':0.5, 'pad':10})

    ax[0,1].text(-0.05, -0.025, r'$\frac{%0.2e}{\lambda^{4}}$' %(res[-1].x[0]), style='italic',fontsize=16,
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

    f.suptitle("Rayleigh Scattering Cross Section for N2",fontsize=18)

    plt.show()
