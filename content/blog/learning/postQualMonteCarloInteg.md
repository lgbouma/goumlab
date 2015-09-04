Title: Computational Physics with Python
Slug: qual-MCint
Date: 2015-09-04
Tags: tests, python, monte-carlo
Summary: We talk a bit about tests, and look at a funny numerical integration method.

# Written quals, and the point of exams

So I took a portion of my grad program's qualifying exam this morning. The whole process of "qualifying" to be degree candidate entails taking a written exam (four parts: classical mechanics, statistical mechanics, electromagnetism, and quantum mechanics) and afterwards being grilled by a faculty panel in an oral exam. 

Honestly the whole thing was a bit underwhelming, given how difficult some of the practice problems were. I was talking to a faculty member about the process, and his perspective was essentially: the exam is a tool to get you to study, which you do to learn the material. My opinion is that while it can be worthwhile to have challenging exams to assess the depth of what you actually learned, there's only so much you can expect out of someone in a short time period. "Easy exams" are a basic check on whether or not you have studied. Deep understanding, acknowledged by yourself as well as your peers, is the real test. As long as a candidate approaches an exam precisely as a way of learning the material (in lieu of a hurdle to pass, potentially skimming the material to pass the test), I don't think there's too much lost in providing exams where a large proportion of the test-takers pass. 

# Monte-Carlo Integration

I was reading a section of [Mark Newman's textbook](http://www-personal.umich.edu/~mejn/cp/chapters.html) that I hadn't covered in the class previously, and he describes an integration method that's actually pretty hilarious, and is really simple.

It called Monte-Carlo integration: you have some bounded function *f(x)* you want to integrate over an interval *I=[a,b]*, but *f* is poorly behaved on the interval. It might even be pathological, for instance oscillating infinitely between say 0 and 1 when near the edges of the interval. All the standard integration techniques -- the trapezoidal rule, Newton's method, Gaussian integration, etc. -- will fail quite badly in these highly oscillatory regions. 

Monte Carlo integration says: the area bounded by *f(x)* on its graph is surely finite. It's just some fraction of the area of the rectangle of area *(b-a)* (where we assume that *f* is taking values between 0 and 1, but any bounded function can be scaled to this). Well, so pick a random number *x* on *I*, and another random number *y* on the domain of *f*. If *f(x)<y*, then we're below the curve. If not, we're above it. Repeat this process many times, keeping track of what fraction of the time we're below the curve, and what fraction we're above it. Since we know the area of the rectangle the whole thing happens in (this method obviously scales for any dimension), the fraction of hits below the curve multiplied by the total area we're allowing our points to range over is precisely our estimate for the integral.

A cute implementation of this for a pathological function is below:

::: python
	# Idea: have a pathological function (varies infinitely fast near edges).
	# Throw a bunch of points at the function, randomly.
	# The ones that land below it contribute to an estimate of the area.

	from math import sin
	from random import random

	def f(x):
	    return (sin(1/(x*(2-x))))**2

	N = 10000
	count = 0
	for i in range(N):
	    x = 2*random()  # domain is [0, 2)
	    y = random()
	    if y<f(x):
		count += 1

	I = 2*count/N
	print(I)

The one issue, as you might expect, is that this method isn't very accurate. It turns out that it scales the inverse square root of the number of points you throw at the function. 
