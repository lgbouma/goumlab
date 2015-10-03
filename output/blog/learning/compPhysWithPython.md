Title: Computational Physics with Python
Slug: classRev-compPhysPython
Date: 2015-08-13
Tags: computation, python, physics, class, review
Summary: We discuss a class we took online, and post transcribed notes and homeworks.

Okay. So given the substantial chunk of free time that precedes graduate school, what are you going to do with it? I thought one cool thing would be to learn some numerical methods for physics calculations. I've worked in computational physics, but mostly in C++. This can be a bit of a pain, in that the code can make the mathematics opaque, particularly when the math methods are new.

Python fixes this problem. At first glance, it's practically a scripting language. It's interpreted, so you don't need to compile your programs before running them. It also has dynamic typing, which means one less thing to worry about vs. C++. The libraries (notably `numpy`, `scipy`, and `matplotlib`) are well-developed and incredibly easy to work with.

So I decided to work through a class I found on the world wide web: [Mark Wilde's Phys7411](http://www.markwilde.com/teaching/2015-spring-phys7411/). The class uses [Mark Newman's textbook](http://www-personal.umich.edu/~mejn/cp/chapters.html), which is quite good. I wound up buying the book when I was about 3/4 done with the course, since only the beginning five or six chapters are free online.

I wrote up some notes and my homeworks, linked at the bottom of this post.

# Approach
My method for working the material was roughly as follows:

* Read and transcribe lecture notes, ~5 lectures at a time (total: 20)
* Work through corresponding homework set (total: 5)
* Repeat

The reason for the transcription (vs. just reading and coding) was that I wanted to figure out a new note system, using a mix of [BaKoMa TeX](http://www.bakoma-tex.com/) and OneNote for live-typesetting notes. Once I was through like five lectures it became a matter of momentum, and the type-setting got faster as I worked more with the software.

# Assessment (incoming wall of text)
Our goals were basically

1. Learn how to approach and solve physics problems with computers,
2. Develop fluency with the BaKoMA TeX editor, and
3. Develop fluency with Python.

How did we do? We read and transcribed Mark Wilde's lectures, and did four of his five homeworks. I might get on to doing the last one, but for now I want to get on to reassessing what I should be doing with my time before the semester starts. This blog is part of that.

Vis-a-vis goal 2, we did pretty well. The notes are attached, and they look good. We have good LaTeX methods for code integration, figures, and a *lot* of custom-macros for live type-setting. Writing math is pretty good, but it’ll never be as abstract as free-hand on paper. This makes sense. If you want to think precisely (or myopically), typesetting on BaKoMa will be a good tool. However, if you want depth, and abstraction, and internalization, you need to worry about note-taking gaining an upper-edge on the learning. Often, you'll want to be focusing on the concepts and ideas, rather than one the pretty notes.

So what? So the rule of thumb is: if it’s extremely idea-dense, (in addition to being hard to typeset), then handwritten. And since a good number of my classes will be idea dense, they’ll be hand-written. Post-lecture, I can summarize or process those notes in BaKoMa, something like 30mins-1hr/lecture (which is also good lecture review).

What about goals 1 and 3? Well let’s talk about the Python side first. I gained some real familiarity with `numpy` and `matplotlib`, but not really `scipy` at all. The libraries read very similar to previous libraries I’ve worked with (especially in JDFTx) which is nice. There are still obviously major parts of just `numpy` that I don’t have a good grasp on, and that are important for being able to do basic tasks in Python (e.g., array manipulation, working with dictionaries, creating UI’s). 

But I like Python. I think that I’ll keep working on it. At the same time, I’ll be able to learn physics through it. How do I mean? Well, I see a new concept, or some new differential equation, and I’ll be able to simulate it. That’s the point! Obviously, not a lot of textbooks or classes are catered to numerics. That’s both the challenge and the opportunity -- it’s building myself into a 'Π-shaped' practitioner: I’ll need to develop real depth in both the field-specifics, as well as in the numerical/computational realizations of those specifics.

I think it’s really telling that I could have gotten through my undergrad without having ever seen something like the trapezoidal rule (it was only through external research that I didn't). Maybe it was implicit in calculus, and so I saw it and ‘internalized’ it a long time ago. But why did I never build on it? Why did no one ever mention you could actually *do it* on a computer? And that you should *want to*? Well, this is about fixing that.

Finally, on ‘approaching and solving physics problems with computers’: that’s obviously a high bar. I did solve some toy problems. And I think the methods I’ve seen will continue to be useful: time-propagating differential equations (e.g., with Runge-Kutta) is immensely useful, as is being able to numerically evaluate integrals. Spending some time on Fourier transforms was also important. Also, I basically wrote a computational solver to the time-independent Schrodinger equation, for arbitrary potentials. That’s something you could never get close to, analytically. Being able to manipulate arrays of data (e.g., Fourier transforms, iterating operations, plotting) is also immensely practical. 

Basically, there needs to be a balance between the field-specific knowledge and the computation knowledge (hence, this blog's structure). I think there’s a Python rabbit hole that I’m only just beginning to jump down, but the analytical methods I know are far from useless. In fact, they’re essential to be able to do any kind of independent scientific computation. And that kind of computation is the right kind of challenge: it says ‘you should value being able to explain things to computers, because they’ll help you understand more material, at greater depth, and with greater efficiency’.

[Lecture notes]({attach}/downloads/pdfs/compPhysPython.pdf)

Homework solutions (about 80% done):

[HW1]({attach}/downloads/pdfs/hw1soln.pdf)

[HW2]({attach}/downloads/pdfs/hw2soln.pdf)

[HW3]({attach}/downloads/pdfs/hw3soln.pdf)

[WH4]({attach}/downloads/pdfs/hw4soln.pdf)


And here's a nice photo from HW3:

![Photo Name]({attach}/blog/images/hw3crop.png)
