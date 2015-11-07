Title: Exoplanet distributions in matplotlib
Slug: classic-matplotlib
Date: 2015-08-15 21:40
Tags: open-exoplanet-catalog, plotting, python, matplotlib
Category: exoplanets
Summary: We make a plot of exoplanet mass vs. semi-major axis for like, 2000 exoplanets!

A classic plot in exoplanet astronomy looks at the masses of exoplanets against their semi-major axes. I figured I would try playing around with the data available from the [Open Exoplanet Catalog](https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue/) to see if I could replicate these. This served as an exercise in `matplotlib`, as well as in learning about the exoplanet field. The result follows below, where every point represents an exoplanet:

![Mass_vs_semiMaj]({attach}/blog/images/mass_vs_semiMajAxis_custom1.png)

We remark that: (1) wow, that's a lot more planets than anyone could claim
20 years ago. (2) We can pretty clearly see some of the biases of the different
planet finding techniques as they stand. The transit (photometry) method
is biased towards short-period planets that actually pass in front of their stars
in a reasonable time. The planets we can currently directly image are much further out, away
from their star's glare, and are quite large. The planets whose Doppler signals
are easiest to monitor are also at large masses, in between the distance sensitivities
of the transit and direct imaging methods. Finally, the microlensing planets
have much greater spread in mass, and can actually probe somewhat lower masses than 
the RV method at greater distances from the host stars.

Also, points for guessing what those "other" planets are (notice the peculiar
semimajor axis of one of them).
 
The code for generating this figure is available [here]({attach}/downloads/python/fig1.py). You'll need to also use this [matplotlibrc file]({attach}/downloads/python/matplotlibrc). I did it all in 2.7, but you should be able to figure it out for 3.X if you're trying it out for yourself.

Before signing off, I think it's worth remarking on how much work it took the astronomy community to obtain all this data. The first detections of exoplanets were twenty years ago, and since then the community has confirmed around 2000 planets. Today I can put together a plot like this in an hour or two. These timescales are a drop in the bucket compared to how long the planets themselves have been around, perhaps even unobserved until we looked at them (or perhaps not! Both are interesting prospects). Thanks to the astronomers and OEC group for making this all available!
