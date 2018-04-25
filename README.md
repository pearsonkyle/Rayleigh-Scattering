# Rayleigh-Scattering
Empirical fits to Rayleigh scattering cross section measurements in historic data (~300-900 nm). 


## Introduction 
Rayleigh scattering results from the electric polarizability of the particles. The oscillating electric field of a photon acts on the charges within a particle, causing them to move at the same frequency. The particle therefore becomes a small radiating dipole whose radiation we see as scattered light. Rayleigh scattering of light is done typically by particles much smaller than the wavelength of the radiation (x << 1).

![scattering regime](https://wikimedia.org/api/rest_v1/media/math/render/svg/e881ee39e1776b6a1af521b8552a9d50ac4fe4d8)

Here r is the characteristic length of your particles (e.g. H2, Dust, etc..) and lambda is the wavelength of light. We test analytic expressions for the Rayleigh scattering cross section against experimentally determined values. We find discrepencies between analytic derivations and experimental measurements up to 5% or more so we only report empirical fits in our results below. 

## Analysis
I test two different analytic expressions to model the wavelength dependence of molecular cross-sections at visible wavelengths. I test a single order and third order approximation. Data is optimized using a simplex solver, Nelder Mead, where the chi-squared and percent error are optimized. I find the best metric to minimize regarding the fit to lab measurements is the percent error because the cross-sections span orders of magnitude the chi-squared calculation will be biased towards optimized the larger magnitude data over the smaller magnitude. Thus the best fit (via percent error minimization) is shown in red (for single order approximation) and orange (third order). 

## Results
The top left subplot has the measured values for a
![Cross Section for H2](https://github.com/pearsonkyle/Rayleigh-Scattering/blob/master/Figures/h2.png) 
![Cross Section for CO2](https://github.com/pearsonkyle/Rayleigh-Scattering/blob/master/Figures/co2.png)
![Cross Section for N2](https://github.com/pearsonkyle/Rayleigh-Scattering/blob/master/Figures/n2.png)


## How to use
1. import the class from [rayleigh.py](https://github.com/pearsonkyle/Rayleigh-Scattering/blob/master/rayleigh.py)
2. define your molecule and wavelength region
3. ???
4. Profit from your cross section values
```python
import numpy as np
from rayleigh import rayleigh

if __name__ == "__main__":
    molecules = [ rayleigh('H2'), rayleigh('CO2'), rayleigh('N2') ]
    waves = np.linspace(3000,5000,100)

    for i in molecules:
        print("{} {:.3e} cm2".format( i.name, i.cross_section(waves)[0] ))
```



## References
- [ [1] Historic Rayleigh Scattering Measurements (Ford 1973)](http://www.sciencedirect.com/science/article/pii/S0092640X73800117?via%3Dihub)
- http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1962ApJ...136..690D&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf
- [2] http://pds-atmospheres.nmsu.edu/education_and_outreach/encyclopedia/rayleigh_optical.htm
- https://refractiveindex.info/?shelf=main&book=CO2&page=Bideau-Mehu
- https://books.google.com/books?id=FeoLkDrNY2MC&pg=PA85&lpg=PA85&dq=depolarization+factor+for+H2&source=bl&ots=5bQTMi1Pw8&sig=WUc8OM6Va9N2JShvzHc4ZCJOGWY&hl=en&sa=X&ved=0ahUKEwjc5tfT0dbTAhVDyGMKHZbCBvsQ6AEIJzAA#v=onepage&q=depolarization%20factor%20for%20H2&f=false
- http://irina.eas.gatech.edu/ATOC5235_2003/Lec9.pdf
