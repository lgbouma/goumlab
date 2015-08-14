Title: Plotting a classic in matplotlib
Slug: classic-matplotlib
Date: 2015-08-15 21:40
Tags: open-exoplanet-catalog, plotting, python, matplotlib
Category: learning, exoplanets
Summary: We make a plot of exoplanet mass vs. semi-major axis for like, 2000 exoplanets!

A classic plot in exoplanet astronomy looks at the masses of exoplanets against their semi-major axes. I figured I would try playing around with the data available from the [Open Exoplanet Catalog](https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue/) to see if I could replicate these. This also served as an exercise in `matplotlib`. The result follows below, where every point represents an exoplanet:

![Mass_vs_semiMaj]({attach}/blog/images/mass_vs_semiMajAxis_custom1.png)

And splitting up the different planet-finding methods for clarity:

![Different_techniques]({attach}/blog/images/mplMassSemiMajDiscTypeSegmented.png)

The code for generating these figures is available here ([first figure]{attach}(/downloads/python/fig1.py)) and here ([second figure]{attach}(/downloads/python/fig2.py)). You'll need to also use this [matplotlibrc file]({attach}/downloads/python/matplotlibrc). I did it all in 2.7, but you should be able to figure it out for 3.X if you're trying it out for yourself.

I'll analyze these plots in depth in the future, but signing off, I think it's worth remarking on how much work it took an incredibly dedicated community of astronomers to get all this data. The first detections of exoplanets were twenty years ago, and today I can put together a plot like this in a few hours' effort. And these timescales are a drop in the bucket compared to how long the planets themselves have been around. Thanks to the astronomers and OEC group for making this all available!
