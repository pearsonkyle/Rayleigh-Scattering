# Rayleigh-Scattering
Empirical fits to Rayleigh scattering cross sections for H2, CO2 and N2 measurements (~300-900 nm). 


## Introduction 
Rayleigh scattering results from the electric polarizability of the particles. The oscillating electric field of a photon acts on the charges within a particle, causing them to move at the same frequency. The particle therefore becomes a small radiating dipole whose radiation we see as scattered light. Rayleigh scattering of light is done typically by particles much smaller than the wavelength of the radiation (x << 1).

![scattering regime](https://wikimedia.org/api/rest_v1/media/math/render/svg/e881ee39e1776b6a1af521b8552a9d50ac4fe4d8)

Here r is the characteristic length of your particle (e.g. H2, dust, etc..) and lambda is the wavelength of light. Rayleigh scattering preferentially scatters more light at bluer wavelengths than red light due to the blue side having a larger cross section (one of the reasons the sky is blue). 

## Analysis
In this analysis, I compare an analytic derivation for the Rayleigh scattering cross section using index of refraction measurements with experimental cross section measurements. A power law of first and third order are used to model the experimental cross section measurements and then are compared to the analytic expression. The power law uses a wavelength to the negative fourth power based on the analytic derivation of the cross section however the coefficients are optimized from the fitting routine. I use a simplex method, Nelder-Mead, to optimize the parameters in the power law. In each fit to the experimental data, the sum of the absolute value of the percent error is minimized. I use the percent error as opposed to a more traditional metric like the chi-squared because the data spans orders of magnitude. In my experimentation, I found that minimizing the chi-squared would only give me a good fit where the data had a large value (e.g. the bluer wavelengths) and it would not fit the red side as well since it was 2 orders of magnitude smaller. The percent error is less susceptible to this variation since the metric is normalized by the data value thus removing the magnitude (or more) variation. The best fit (via percent error minimization) is shown in red (for single order approximation) and orange (third order). I find discrepencies between the analytic derivation and experimental measurements up to 5% or more. I would suggest using the empirical fit over the analytic derivation in future calculations. One could also use an interpolation between the experimental data however you would be constrained to the wavelength region of the measurements and extrapolating beyond this region can lead to large uncertainties when using a linear or quadratic method. My empirical fit allows you to extrapolate beyond this region following an equation with the same wavelength dependence as the analytic derivation.   


## Results
The values in the legend correspond to the sum of the absolute value of the y-axis. (e.g. sum of |% percent error|) 
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
    waves = np.linspace(3000,5000,100) # angstrom

    for i in molecules:
        print("{} {:.3e} cm2".format( i.name, i.cross_section(waves)[0] ))
```



## References
- [ [1] Rayleigh Scattering Measurements of H2 (Ford 1973)](http://www.sciencedirect.com/science/article/pii/S0092640X73800117?via%3Dihub)
- [ [2] Absolute Rayleigh scattering cross sections of gasses (NASA 1977) ](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19770012747.pdf)
- [ [3] Temperature dependence on Rayleigh scattering of H2](http://adsabs.harvard.edu/abs/1962ApJ...136..690D)
- [ [4] Rayleigh Scattering derivation pt1. ]( http://pds-atmospheres.nmsu.edu/education_and_outreach/encyclopedia/rayleigh_optical.htm)
- [ [5] Rayleigh scattering derivation using wavelength dependent index of refraction ](https://books.google.com/books?id=FeoLkDrNY2MC&pg=PA85&lpg=PA85&dq=depolarization+factor+for+H2&source=bl&ots=5bQTMi1Pw8&sig=WUc8OM6Va9N2JShvzHc4ZCJOGWY&hl=en&sa=X&ved=0ahUKEwjc5tfT0dbTAhVDyGMKHZbCBvsQ6AEIJzAA#v=onepage&q=depolarization%20factor%20for%20H2&f=false)
- [ [6] Optical constants for molecules](https://refractiveindex.info/?shelf=main&book=CO2&page=Bideau-Mehu)

## Reproducibility
All work including experimental measurements are supplied in the folders marked by the molecule's notation. 

## Citing this repository
Please cite the following article if you make use of this code and smash that star button

[Ground-based Spectroscopy of the Exoplanet XO-2b using a Systematic Wavelength Calibartion](https://arxiv.org/abs/1811.02060)

Here is an example bibtex (as of 12/21/2018)
```
@ARTICLE{Pearson2018,
       author = {{Pearson}, Kyle A. and {Griffith}, Caitlin A. and {Zellem}, Robert T.
        and {Koskinen}, Tommi T. and {Roudier}, Gael M.},
        title = "{Ground-based Spectroscopy of the Exoplanet XO-2b using a Systematic
        Wavelength Calibration}",
      journal = {arXiv e-prints},
     keywords = {Astrophysics - Earth and Planetary Astrophysics},
         year = 2018,
        month = Nov,
          eid = {arXiv:1811.02060},
        pages = {arXiv:1811.02060},
archivePrefix = {arXiv},
       eprint = {1811.02060},
 primaryClass = {astro-ph.EP},
       adsurl = {https://ui.adsabs.harvard.edu/\#abs/2018arXiv181102060P},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```
