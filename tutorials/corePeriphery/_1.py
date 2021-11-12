# ! /usr/env/bin python3
# -*- encoding utf-8 -*-

"""
--------------------------------------------------------------------------------
   _1.py    |    using closeness centrality as a measure of node coreness
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk

Dates: created Fri 25 Oct 09:26:01 2019
       last change Sun Oct 27 11:00:08 UTC 2019

Notes: Numpy and Networkx are required libraries

"""

# %% setup
import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


# %% simulate the network
'''
Drawing on the adjacency matrix reported in Borgatti and Everett's paper, we
can think an indirected cp network as the composition of:
- a square (n1 X n1), very densely populated matrix reflecting ties linking any
  two core nodes
- a 'rectangular' (n1 X n2) matrix reflecting scatter ties linking peripheral
  nodes to core nodes
- a square (n2 x n2), matrix mostly populated by zeros, which reflects absent
  ties among peripheral nodes
'''

# simulation params
n = 1000                              # nodes
c = 0.05                              # % core nodes
p = 1 - c                             # % peripheral nodes
n_c, n_p = int(n * c), int(n * p)     # core nodes, peripheral nodes

# core - core ties
cc = np.ones((n_c, n_c))

# periphery - core ties
pc = np.random.binomial(1, 0.1, size=(n_p, n_c))

# core-periphery ties
cp = np.transpose(pc)

# periphery - periphere y ties
pp = np.zeros((n_p, n_p))
np.fill_diagonal(pp, 1)                # filling the diagonal with 1s

# stack the three matrices
cc_pc = np.vstack((cc, pc))            # stack left-bottom and left-top
cp_pp = np.vstack((cp, pp))            # stack right-bottom and right-top
a = np.hstack((cc_pc, cp_pp))          # stack left and right sections

# get a Graph class object 
g = nx.from_numpy_array(a)

# %% get a continuous indicator of coreness, i.e., the extent to which a node
#    is close to other central nodes. For an example, see:
#    https://www.researchgate.net/publication/338223948_Core-Periphery_Tension_in_Online_Innovation_Communities
coreness = nx.algorithms.centrality.closeness_centrality(g)
