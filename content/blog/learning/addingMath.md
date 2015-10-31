Title: Adding math!
Date: 2015-10-30
Slug: math-temp
Tags: LaTeX
Summary: Adding math typesetting to the blog

# Temp math test
We're trying out the pelican render-math plugin, available
[here](https://github.com/barrysteyn/pelican_plugin-render_math).

Here are equations, like $a^2=b^2+c^2$, which should be rendered inline.
We notice that we shouldn't put white space or else it won't render.

Putting together another equation, but now centered:
$$E^2=p^2c^2+m^2c^4$$
in units where $c$ is not equal to 1. If we set $c=1$, then
$$E^2=p^2+m^2.$$ 
Much nicer.

Apparently, we can go even further with this pelican extension though.
we can actually treat our markdown document like a latex documention
doing something like
\begin{equation}
\exp x = \sum_n \frac{x^n}{n!}
\label{eq:expSum}
\end{equation}
in an equation environment, and then go back and label Eq. $\ref{eq:expSum}$.
We'll see!

Baby steps.
