# Network Analytics, SMM638 ― README

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Instructor](#instructor)
- [Module Overview](#module-overview)
- [Materials & Readings](#materials--readings)
- [Learning Objectives](#learning-objectives)
- [Assessment](#assessment)
  - [Mid-term project](#mid-term-project)
  - [Final course project](#final-course-project)
  - [Case studies](#case-studies)
  - [Discretionary problem sets](#discretionary-problem-sets)
- [Schedule of the Module](#schedule-of-the-module)
- [Guest speakers](#guest-speakers)
- [Prerequisites](#prerequisites)
- [Software Requirements](#software-requirements)
- [Versioning](#versioning)

<!-- /TOC -->

# Instructor

+   Dr. Simone Santoni ―  [simone.santoni.1@city.ac.uk](simone.santoni.1@city.ac.uk)
+   Office hour: every Thursday from 12:00 to 13:00 (students are required to book a slot and share their questions via email in advance).
+   Teaching assistant: Dr. Matteo Devigili ―  [matteo.devigili.2@city.ac.uk](matteo.devigili.2@city.ac.uk)

# Module Overview

Networks are ubiquitous: job offerings reach us via inter-personal
connections; what we see on the screen of our digital device is a
function of the relationships we develop in the digital world; market
valuations are ― largely ― the byproduct of social influence, which
accumulates and spreads over relations. This module provides students
with cutting-edge network theories and practical tools to appreciate the
organization and functioning of disparate networks. Ultimately, the goal
is to develop a distinctive angle on how networks bring value to
individuals, organizations, and communities.

# Materials & Readings

For this module, students are not required to purchase any (expensive)
book, whereas it is essential they carefully go through the following:

-   lecture notes (to be uploaded onto
    Moodle/[Github](https://github.com/simoneSantoni/net-analysis-smm638)
    weekly; they include slideshows + videos);
-   selected chapters from [Networks, Crowds,
    Markets](https://www.cs.cornell.edu/home/kleinber/networks-book/)
    (access via our Library websiste)
-   selected chapters from [Network
    Science](http://networksciencebook.com/) (access via the Book
    website)

Discretionary readings students may want to reference to:

-   How networks matter:
    [Linked](https://www.amazon.co.uk/Social-Network-Analysis-Applications-Structural/dp/0521387078)
-   Mathematical foundations of network analytics: [Introduction to
    Graph Theory](https://www.amazon.co.uk/Introduction-Graph-Theory-Dover-Mathematics/dp/0486678709/ref=sr_1_1?s=books&ie=UTF8&qid=1538502346&sr=1-1&keywords=graph+theory)
-   Social network analysis metrics: [Social Network Analysis: Methods
    and Applications](https://www.amazon.co.uk/Social-Network-Analysis-Applications-Structural/dp/0521387078)
-   Journal articles (to be uploaded onto Moodle/[Github](https://github.com/simoneSantoni/net-analysis-smm638)
    weekly)

# Learning Objectives

At the end of the module, students should be able:

-   to appreciate the properties of networks;
-   to appreciate the properties of communities of nodes belonging to a
    network;
-   to appreciate the properties of individual nodes belonging to a
    network;
-   to visually represent the key features of networks;
-   to leverage the most advanced Python modules for network analytics;
-   to mobilize key network analytics notions and tools in order to
    produce elegant, effective, and efficient solutions to practical
    problems in the field of business strategy, product innovation, and
    operations.

# Assessment

As per the module specification, students will be assessed on the basis
of coursework submissions, which all are the outcome of group-level
efforts (yes, you understand correctly, for this module there is no
final examination and you are not supposed to deliver any assignment on
your own). Specifically, there are three pieces of coursework, namely:

+   a 'mid-term project' (MTP)
+   a 'final course project' (FCP)
+   two case studies (CS)

These three pieces of coursework contribute to the final mark (FM) as follows:

FM = 0.20 X MTP + 0.75 X FCP + 0.05 X [(CS1 + CS2)/2]

All types of assessment will be evaluated along four criteria: i)
appropriate use of notions and frameworks discussed in class; ii)
effectiveness of the proposed answer or solution; iii)
originality/creativity of the proposed answer or solution; iv)
organization an clarity of submitted materials. All criteria carry-out
equal weight in terms of mark.

## Mid-term project

For the **MTP**, groups are required to solve a network analytic problem. The
details of the MTP will be available by week 3, when the project will be
released. Submissions will be assessed on a 0 - 100% scale. The Groups who
fail MTP can resubmit a revised version of the project; if the revision is
sufficient, students receive a 50% mark. The deadline for the project is
November 9 (week 6). Selected groups will be invited to present the outcome of
their work to fellow students in week 6. Invited groups could also receive a
maximum of 3 bonus points on the basis of the quality of their presentations.

## Final course project

With the **FCP**, groups make their hands 'dirty' as they help a real-world
client to face some network analytic challenges. The details about the client
and the challenge will be available in week 7. Final course projects will be
evaluated on a rolling-based window and should be submitted by mid December
(the course office will confirm the exact deadline shortly).

## Case studies

Case studies provide students with the opportunity to learn how to integrate
the 'business' and the 'network analytic' perspectives in order to  deal
effectively with real-world problems. In terms of process, groups of students
will receive i) a detailed description of a business issue, and ii) relevant
data; then, they will be working for one week to produce their own solution.
Solutions will be disclussed in class. Each presenting group will be
associated with a discussant group whose role is to challenge the ideas,
tools, and recommendetions that will be brought to the table. I expect six
pairs of presenting and discussant groups; this means group that will present
their solution in week 8 will serve as discussant in week 10 (and viceversa).
Both presenting and discussant groups will be assessed.

## Discretionary coursework

**Problem sets** will be launched weekly. Students may want to deal
these problem sets and present their solution to the class. Up to three students
per session will be selected on the basis of the novelty and
effectiveness of the proposed solution. One bonus point
(+1 FM) will be assigned.

# Schedule of the Module

| Week | Topic                                              |
|:----:|:---------------------------------------------------|
|  1   | Introduction to SMM638                             |
|      | Introduction to networks                           |
|      | - how networks matter                              |
|      | - networks are made-up of nodes and ties           |
|      | - graph and algebraic representations of networks  |
|      | - forms of networks                                |
|      | Debate:                                            |
|      | - markets & networks: the Soundcloud example       |
|  2   | Network theory                                     |
|      | - strong ties and closure                          |
|      | - weak ties and brokerage                          |
|      | Network models and metrics                         |
|      | - centrality                                       |
|      | - paths and distances                              |
|      | - connectedeness                                   |
|      | Laboratory (NetworkX)                              |
|  3   | Network therory                                    |
|      | - small worlds and networks                        |
|      | - core-periphery structures in networks            |
|      | - community structures in networks                 |
|      | Network models and metrics                         |
|      | - search and collective intelligence in networks   |
|      | Laboratory (NetworkX)                              |
|      | Mid-term project release                           |
|  4   | Network theory                                     |
|      | - homophily, selection, and social influence       |
|      | Network models and metrics                         |
|      | - closure and link formation in online communities |
|      | - spatial models of segregation                    |
|      | Laboratory (NetworkX and Mesa)                     |
|  5   | Network theory                                     |
|      | - scale-free networks                              |
|      | - preferential attachment                          |
|      | - Barabasi-Albert model                            |
|      | Network models and metrics                         |
|      | - crowds and popularity                            |
|      | - networks, recommenders, and popularity           |
|      | Laboratory (NetworkX)                              |
|  6   | Mid-term project - students' presentations         |
|      | Laboratory (Graph-Tool)                            |
|      | - efficient network analysis with Graph-Tool       |
|  7   | Final course project release                       |
|      | Network theory                                     |
|      | - cascading behavior                               |
|      | - diffusion in and through networks                |
|      | Network models and metrics                         |
|      | - spreading phenomena                              |
|      | Laboratory (NetworkX, Graph-Tool)                  |
|  8   | Case study #1 (associated with section 7 topics)   |
|  9   | Network theory                                     |
|      | - percolation theory                               |
|      | - network robustness                               |
|      | Network models and metrics                         |
|      | - attack tolerance                                 |
|      | - cascading failures                               |
|      | Laboratory (NetworkX, Graph-Tool)                  |
|  10  | Case study # 2 (associated with section 9 topics)  |


# Guest speakers

Throughout all the various weeks of the Term, SMM635 will host two types of
guest speakers: ambassadors – former students of the BA program – and
practitioners from several industries.


# Prerequisites

The SMM692 ― Python Pre-Course module defines the knowledge students
should possess in order to proficiently attend to SMM638 ― Network
Analytics.

# Software Requirements

For this module you are supposed to run Python 3.6 on your machine. Now,
how to get Python work on your machine? There are several ways to do
that. A fast, smooth alternative is to install
[Anaconda](https://www.anaconda.com/what-is-anaconda/), an open source
distribution of Python that includes: i) 250+ popular data science
packages; ii) the [conda](https://conda.io/docs/index.html) package,
which makes quick and easy to install, run, and upgrade complex data
science and machine learning environments.

Here is the workflow:

1.  Use your preferred browser to open the link pointing to the
    [Anaconda repository](http://www.numpy.org/);

2.  Select the installer the which suits your machine (32- or 64-bit)
    and operating system (Win, Mac OS, Linux). Mac users may want to
    download the graphical installer rather than the command-line
    installer (students may feel less comfortable with);

3.  Retrieve the installer (perhaps in your download folder);

4.  Run the installer;

5.  Log-out from your current session (it does not matter if you use
    Win, Mac OS or Linux);

6.  Log-in into a new session;

7.  Run 'Anaconda Navigator'―namely, a convenient place to launch the
    IPython shell or other user-interfaces to interact with IPython.

On top of Anaconda ― Python, students should install the modules:

+   [NetworkX](https://networkx.github.io/)
+   [Mesa](https://mesa.readthedocs.io/en/master/)
+   [Graph-Tool](https://graph-tool.skewed.de/). Note Graph-Tool is a 'complex' library (i.e., it depends on several Pyhon and C++ libraries); you may want to follow the installation instructions reported under the [`resources`](https://github.com/simoneSantoni/net-analysis-smm638/tree/master/resources/graphTool) section of this repo.

# Versioning

+ Created: 28/09/2020, 06:06:45  
+ Last change: no revisions so far
