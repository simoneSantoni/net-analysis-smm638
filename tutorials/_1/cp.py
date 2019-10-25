# ! /usr/env/bin python3
# -*- encoding utf-8 -*-

"""
--------------------------------------------------------------------------------
    Core-periphery problem set
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk

Dates: create Fri 25 Oct 09:26:01 2019; last change 

Notes: Numpy and Networkx are required libraries 

"""


# %% setup

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# %% simulate the network

'''
Drawing on the adjacency matrix reported in Borgatti and Everett's paper, we can
think an indirected cp network as the composition of:

- a square (n1 X n1), very densely populated matrix reflecting ties linking any 
  two core nodes
- a 'rectangular' (n1 X n2) matrix reflecting scatter ties linking peripheral 
  nodes to core nodes
- a square (n2 x n2), matrix mostly populated by zeros, which reflects absent
  ties among peripheral nodes
'''

# simulation params
n = 1000
p_c = 0.05
n_c, n_p = n * p_c, n * (1 - p_c)

# core-core ties
cc = np.random.binomial(1, 1, size=(n_c, n_c))

# periphery-core ties
pc = np.random.binomial(1, 0.1, size=(n_c, n_p))



# core-periphery ties


