import numpy as np

def sigma_ray(x,*args):
    # cross sections (cm2), x=wavelength(A)
    return  np.vstack( [ args[i]/x**(4+2*i) for i in range(len(args))] ).sum(0)

class rayleigh(object):
    # returns rayleigh scattering cross section from model fits to data
    def __init__(self,name):
        if name.upper() == 'H2':
            self.name = 'H2'
            self.args = [1.01e-12,3.26e-7,1.47]
        if name.upper() == 'CO2':
            self.name = 'CO2'
            self.args = [1.22e-12,3.26e-6,-14.60]
        if name.upper() == 'N2':
            self.name = 'N2'
            self.args = [3.50e-12,1.22e-5,-21.83]
        else:
            print("Molecule: {} not supported".format(name))

    def cross_section(self,wave):
        # wave in A, return cm2
        return sigma_ray(wave,*self.args)

if __name__ == "__main__":
    molecules = [ rayleigh('H2'), rayleigh('CO2'), rayleigh('N2') ]
    waves = np.linspace(3000,5000,100)

    for i in molecules:
        print("{} {:.3e} cm2".format( i.name, i.cross_section(waves)[0] ))
    
