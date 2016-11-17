Title: On testing; 'shoot-first, clean-up-later' integration
Slug: qual-MCint
Date: 2015-09-04
Tags: quals, python, monte-carlo
Summary: We talk a bit about tests, and look at a funny numerical integration method.

# Written quals, and the point of exams

I took a portion of my grad program's qualifying exam this morning. The whole process of qualifying to be degree candidate entails taking a written exam (four parts: classical mechanics, statistical mechanics, electromagnetism, and quantum mechanics) and afterwards being grilled by a faculty panel in an oral exam. This morning was a single section of
the written exam.

Honestly the whole thing was underwhelming, given the difficulty of some past exams.
I spoke with a faculty member about the process, and his perspective was essentially: the exam is a tool to get you to study, which you do to learn the material. While it can be worthwhile to have challenging exams to assess the depth of what you actually learned, there's only so much you can expect out of someone in a short time period. "Easy exams" are thus simply a check on whether or not you have studied. Deep understanding, acknowledged by yourself as well as your peers, is the real test. As long as a candidate approaches an exam precisely as a way of learning the material (in lieu of a hurdle to pass, potentially skimming the material to pass some test), I don't think there's too much lost in providing exams where a large proportion of the test-takers pass. By the same logic though, there isn't much harm in writing a very hard test that everyone fails. In fact, the latter is a much more realistic
assessment of what you can and cannot do.

# Monte-Carlo Integration

In unrelated news, I was reading a section of [Mark Newman's textbook](http://www-personal.umich.edu/~mejn/cp/chapters.html) that I hadn't covered in the class previously, and he describes an integration method that's both hilarious and simple.

It called Monte-Carlo integration: you have some bounded function $f(x)$ you want to integrate over an interval $I=[a,b]$, but $f$ is poorly behaved on the interval. It might even be pathological, for instance oscillating infinitely between say 0 and 1 when near the edges of the interval. All the standard integration techniques -- the trapezoidal rule, Newton's method, Gaussian integration, etc. -- will fail quite badly in these highly oscillatory regions.

Monte Carlo integration says: the area bounded by $f(x)$ on its graph is surely finite. It's just some fraction of the area of the rectangle of area $(b-a)$ (where we assume that $f$ is taking values between 0 and 1, but any bounded function can be scaled to this). Well, so pick a random number $x$ on $I$, and another random number $y$ on the range of $f$. If $f(x)<y$, then we're below the curve. If not, we're above it. Repeat this process many times, keeping track of what fraction of the time we're below the curve, and what fraction we're above it. Since we know the area of the rectangle the whole thing happens in (this method obviously scales for any dimension), the fraction of hits below the curve multiplied by the total area we're allowing our points to range over is precisely our estimate for the integral.

Here's a cute implementation (taken from Mark Newman's textbook) of this method for a pathological function:

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

The one issue, as you might expect, is that this method isn't very accurate. It turns out that it scales in accuracy as the inverse square root of the number of points you throw at the function. But in cases where other standard methods fail, this is pretty nice.

To-do for building the website:

1. Figure out LaTeX compatibility.
2. Figure out a better figure embed method.
3. Add comments!
