# Tutorial 3 – README

This tutorial focuses on hompohily in networks. The setting is a friendship network.
I assume gender is the ascriptive characteristic driving tie emergence.

The Python script `homophily.py` achives what follows:

+ it generates a friendship network that is supposed to be observed network
+ it evaluates the empirical distribution of ties (female-female, female-male, and male-male)
  against simulated data in which the same gender is randomly reshuffled over ties
+ it plots the distribution of cosine similarity scores, which are used to appreciate
  the distance between the empirical and simulated distributions.
