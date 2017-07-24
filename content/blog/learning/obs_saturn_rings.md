Title: The Cassini Division
Slug: cassini_division
Date: 2017-07-23
Tags: obs, planets
Summary: I saw a gap in Saturn's rings from my office's telescope!

A week or so ago I took some pictures of Saturn, and after a bit of processing
they show a nifty feature not visible in the [previous
ones](http://lgbouma.com/2017/skystuff.html): a gap!

![cassini]({attach}/blog/images/saturn_ISO500_halfsec_0_heavy_wavelet_rings_5_crop.png)  

More formally, they show the [Cassini
Division](https://en.wikipedia.org/wiki/Rings_of_Saturn#Cassini_Division), the
pixelated black gap between the inner and outer rings. The inner "ring"
(really, rings, but only one provides most of the optical depth) is labelled
"B", the outer "A".  There's a sharp cutoff in the density of the ~cm to m
sized particles at the inner boundary of the division because of a 2:1
resonance with Mimas.

Other (higher resolution) images of [Saturn's rings can be admired
here](https://en.wikipedia.org/wiki/Rings_of_Saturn#Gallery).

I took the images through the 12" Meade LX200 in [Peyton's
Observatory](http://www.astro.princeton.edu/observatory/index.php), using a
Canon EOS 60D. For image acquisition, I used EOS MovRec v0.3.3 (through a
virtual machine), recording in video with half-second exposures at 500 ISO. I
took about 5 minutes of video, which I then ran through Registax 6 and clipped
to the best ~10% of exposures after alignment. I then stacked, ran a
wavelet transform, and cropped, yielding the image you see with your two eyes.
