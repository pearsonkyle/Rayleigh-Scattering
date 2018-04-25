# Rayleigh-Scattering
Empirical fits to Rayleigh scattering cross section measurements in historic data (~300-900 nm). 


## Introduction 
Rayleigh scattering results from the electric polarizability of the particles. The oscillating electric field of a photon acts on the charges within a particle, causing them to move at the same frequency. The particle therefore becomes a small radiating dipole whose radiation we see as scattered light. Rayleigh scattering of light is done typically by particles much smaller than the wavelength of the radiation (x << 1).

![scattering regime](https://wikimedia.org/api/rest_v1/media/math/render/svg/e881ee39e1776b6a1af521b8552a9d50ac4fe4d8)

Here r is the characteristic length of your particles (e.g. H2, Dust, etc..) and lambda is the wavelength of light. Rayleigh scattering preferentially scatters more light at bluer wavelengths than red light due to the blue side having a larger cross section (one of the reasons the sky is blue). 

## Analysis
In this analysis, I test analytic expressions using index of refraction measurements against against experimentally determined cross section values. I find discrepencies between the analytic values and experimental measurements up to 5% or more (see plots below regarding 'refraction'). I would suggest using the experimental fit over the analytic derivation using a wavelength dependent index of refraction for future calculations. 

I test two different analytic expressions to model the wavelength dependence of molecular cross-sections at visible wavelengths. I test a single order and third order approximation. Data is optimized using a simplex solver, Nelder Mead, where the chi-squared and percent error are optimized. I find the best metric to minimize regarding the fit to lab measurements is the percent error because the cross-sections span orders of magnitude the chi-squared calculation will be biased towards optimized the larger magnitude data over the smaller magnitude. Thus the best fit (via percent error minimization) is shown in red (for single order approximation) and orange (third order). 

## Results
ENTER DESCRIPTION HERE
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
- [ [1] Historic Rayleigh Scattering Measurements of H2 (Ford 1973)](http://www.sciencedirect.com/science/article/pii/S0092640X73800117?via%3Dihub)
- [ [2] Temperature dependence on Rayleigh scattering of H2](http://adsabs.harvard.edu/abs/1962ApJ...136..690D)
- [ [3] Rayleigh Scattering Formulation using wavelength dependent index of refraction]( http://pds-atmospheres.nmsu.edu/education_and_outreach/encyclopedia/rayleigh_optical.htm)
- [ [4] Optical constants for molecules](https://refractiveindex.info/?shelf=main&book=CO2&page=Bideau-Mehu)
- [ [5] Absolute Rayleigh scattering cross sections of gasses (NASA 1977) ](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19770012747.pdf)

## Reproducibility
All work including experimental measurements are supplied in the folders marked by the molecule's notation. 
