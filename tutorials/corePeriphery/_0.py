# ! /usr/env/bin python3
# -*- encoding utf-8 -*-

"""
--------------------------------------------------------------------------------
    Core-periphery problem set
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
from graspy.plot import heatmap


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
g = np.hstack((cc_pc, cp_pp))          # stack left and right sections


# %% visualize the core-periphery network
'''
GraSpy (https://graspy.neurodata.io/index.html) is a Python librarary that
leverages Networkx and Matplotlib to create a series of network visualizations
including heatmaps, gridplots, pairplot, degreeplot, edgeplot, screeplot.
As you see below, producing a heatmap of the adjacency matrix at hand takes
one line
'''

# create figure
fig = plt.figure(figsize=(6, 6))

# add plot
ax = fig.add_subplot(1, 1, 1)

# plot data with GraSPy heatmap
heatmap(g, cmap='Greens', ax=ax)

# add title
ax.set_title(r'$A_{ij}$ of the simulated core-periphery network')

# save figure
out_f = os.path.join(os.getcwd(), 'viz_0.pdf')
plt.savefig(out_f)


# %% get degree distribution
# get degree k of each node in g
d = np.sum(g, axis=0)

# get p_k
p_k = np.unique(d, return_index=True)

# plot p_k

# create figure
fig = plt.figure(figsize=(6, 6))

# add plot
ax = fig.add_subplot(1, 1, 1)

# plot data
ax.scatter(p_k[0], p_k[1]/n, alpha=0.4, color='orange')

# transform the scale of axes
#ax.set_xscale('log')
#ax.set_yscale('log')

# labels
ax.set_xlabel(r'$k$')
ax.set_ylabel(r'$p_{k}$')

# title
ax.set_title('Degree distribution of the simulated\ncore-periphery network')

# grid
ax.grid(ls='--')

# save figure
plt.tight_layout()
plt.savefig(os.path.join(os.getcwd(), 'viz_1.pdf'))
