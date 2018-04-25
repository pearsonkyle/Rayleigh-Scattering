# Rayleigh-Scattering
Empirical fits to Rayleigh scattering cross section measurements in historic data (~300-900 nm). 


I test two different analytic expressions to model the wavelength dependence of molecular cross-sections at visible wavelengths. I test a single order and third order approximation. Data is optimized using a simplex solver, Nelder Mead, where the chi-squared and percent error are optimized. I find the best metric to minimize regarding the fit to lab measurements is the percent error because the cross-sections span orders of magnitude the chi-squared calculation will be biased towards optimized the larger magnitude data over the smaller magnitude. Thus the best fit (via percent error minimization) is shown in red (for single order approximation) and orange (third order). 


![A test image](image.png)

## References
- http://www.sciencedirect.com/science/article/pii/S0092640X73800117?via%3Dihub
- http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1962ApJ...136..690D&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf
- http://pds-atmospheres.nmsu.edu/education_and_outreach/encyclopedia/rayleigh_optical.htm
- https://refractiveindex.info/?shelf=main&book=CO2&page=Bideau-Mehu
- https://books.google.com/books?id=FeoLkDrNY2MC&pg=PA85&lpg=PA85&dq=depolarization+factor+for+H2&source=bl&ots=5bQTMi1Pw8&sig=WUc8OM6Va9N2JShvzHc4ZCJOGWY&hl=en&sa=X&ved=0ahUKEwjc5tfT0dbTAhVDyGMKHZbCBvsQ6AEIJzAA#v=onepage&q=depolarization%20factor%20for%20H2&f=false
- http://irina.eas.gatech.edu/ATOC5235_2003/Lec9.pdf
