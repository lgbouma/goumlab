Title: On testing. Oh also, fact-checking The Martian.
Slug: written-exam
Date: 2016-01-30
Tags: tests, electromagnetism, statistical mechanics
Summary: I outline nifty things I learned from qualifying exams.

## The purpose of tests is to learn things.
In an academic test, an examiner learns whether or not
an examinee can perform some task.
The examinee learns the same.
In many cases, all parties concerned then use the difficulty of the task
to infer the test-taker's knowledge or ability in the relevant field.

## Tests are useful beyond school.
In programming, tests teach a programmer whether or not her program works
as expected.
Entire [software design philosophies](https://en.wikipedia.org/wiki/Unit_testing)
stem from the idea that systematic testing is an effective way to write
software.

In the public sphere, IQ tests are indicators
of national prosperity.[^fn-1]
While your personal IQ score barely correlates with your individual outcomes,
your *nation's* mean IQ score is a good predictor of your happiness, how
much money you make, and the efficacy of your government.

In science, testing is the mechanism that ultimately supports
or rejects people's claims about "the way things be". We
elevate this type of testing and call it experimentation.
My personal favorite summary of what scientists do?
**Test and tell**.

## Sorry Matt Damon, you never stood a chance.
In physics, academic tests are presented as "here is a physical situation,
and a few things you might need to know to answer this question.
Now work out some subset of the interesting things you might want to know
about the situation."

For example, consider the scene from *The Martian* when Matt Damon, floating
weightless through space, punctures a hole in his spacesuit to propel himself
à la Iron Man to his crew.[^fn-2]
This situation begs a few questions. Would poking a hole in his spacesuit
actually give Matt Damon enough thrust to make it to the crew?
Would he make it without depleting his air supply?
How can we formulate the mechanism that propels him?

In fact, variants of the above problems were given on the
qualifying exams I just took. The examiners prompted a solution using
statistical mechanics (box with ideal gas inside, how does it effuse?)
but the feasibility of the physics can be understood just as well
from ordinary mechanics.
Specifically, we're told the speed difference between the
Hermes and the MAV is $11\text{m/s}$. In rocket lingo, this means Watney
needs to boost his speed (a *delta-v*) by $11\text{m/s}$.
Let $v_e$ be the exhaust velocity, $m_f \approx 99.95 \text{kg}$ be the final mass
after he ejects *all* the air in his suit, and
$m_i \approx 100 \text{kg} = m_i + \epsilon$ be the initial
mass of Watney plus the air in his suit. I guessed that he has maybe
$50 \text{liter} = 0.05 \text{m}^3$ of air in the suit, which has density about of $1 \text{kg/m}^3$
and thus a mass of about $\epsilon = 0.05\text{kg}$.

Using the [ideal rocket equation](https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation)
(can be derived from Newton's second with a mass that varies in time
with a constant rate), we find
$$\Delta v = v_e \ln (m_i/m_f) = v_e \ln (1 + \epsilon/m_f).$$
In this form, we can Taylor expand ($\ln 1 + x \approx x$) to get
$$\Delta v \approx v_e \epsilon/m_f.$$
Then
$$ v_e \approx \Delta v m_f/\epsilon \approx 11\text{m/s} \times 99.95 \text{kg}/0.05\text{kg} \approx 20,000\text{m/s}.$$

Note that the rocket equation here simplifies to what you would get from
ordinary conservation of momentum, since the Taylor expansion we used on
$\ln(1+x)$ is good enough for small changes in our "rocket's" mass (here,
$\epsilon$ is about a hundredth of its initial mass).

Now I ask you: **is it reasonable to think that gas escaping from an astronaut's
space suit into vacuum will do so at 20 kilometers per second? (about
72,000kph, or one four-thousandth the speed of light)**.

If you want to actually *work out* the speed of the escaping gas, you might
need some statistical mechanics.[^fn-3] Take a box filled with an ideal gas
gas at temperature $T \approx 300\text{K}$
and particle number $N = \rho V / m \approx 0.05\text{kg} /
(28\times 2 \times 10^{-27}\text{kg}) \approx 2\times10^{25}$, where I'm
taking the proton mass to be about $2\times 10^{-27}\text{kg}$ and assuming
air is all nitrogen.[^fn-4]  

The trickier bit is then calculating the flux of particles
(number per unit time per unit area) out of the hole into the vacuum
(assuming none return through the hole).
If you do this, you can work out the average kinetic energy of escaping
particles to be of order $2kT$ for $k$ the Boltzmann constant. From
that energy, I get an escape velocity that's of order
$v_e \sim (4 k T / m)^{1/2} \approx 600 \text{m/s}$. This actually assumes
that the temperature of the gas in the space-suit is constant -- which won't
be true since when the hot molecules leave, the temperature will go down.
However, that just means their escape will impart even less momentum to
Watney, since they'll have lower kinetic energies. The actual escape
velocities will be *lower* than the number we gave.

Sorry Matt Damon, you never stood a chance.

![astronaut]({attach}/blog/images/Astronaut-EVA.png)  
Image: Wikimedia commons, originally NASA.
Inside the suit is Untethered U.S. astronaut Bruce McCandless.

-----
The original purpose of this blog post was going to be a review of cool
things I learned about during qual revision, including:  1. Why from a *dipole* picture we can understand the wavelength-dependence of Rayleigh scattering and thus explain the blue sky and other optical phenomena in the atmosphere. 2. The first trans-Atlantic cable to be laid down, and how it uses water as an outer conductor in a coaxial cable arrangement. 3. The fact that if I hang a rope (or a chain) or chain of constant linear density between two poles, it rests in a shape perfectly described by the hyperbolic cosine function. 4. Why if I shine light at short enough wavelength at a metal, it goes through the metal. 5. How as a rough approximation, treating solids as a bunch of atoms bound together by springs lets me predict almost any relevant physical property you can measure.

I'll write about a few of those in future posts. Until next time!





[^fn-1]: See, for instance, Garett Jones' [Hive Mind](http://www.amazon.com/Hive-Mind-Your-Nation%C2%92s-Matters/dp/0804785961).
Jones argues beyond just correlation for *causation*, *i.e.* that if a nation
has higher IQ, this can *cause* higher national prosperity. The logic is
roughly: nations with higher IQs have more people who are patient,
informed, and cooperative. These tend to be more engaged citizens, and they will
provide more value to their neighbors. Cascading values spread across
communities, and lead to a runaway "hive mind" in which *everyone* winds up
more patient, informed, and cooperative.

[^fn-2]: Note we're talking the movie here. The book explicitly rejected this
idea as being dumb.

[^fn-3]: If you're feeling fancy, you could also formulate the problem
in terms of fluid mechanics. But this is order of magnitude physics.

[^fn-4]: After checking online, I learned that astronauts actually breathe
pure oxygen in spacesuits since nitrogen has no biological function. It's
maintained at about 1/3 of atmospheric pressure.
