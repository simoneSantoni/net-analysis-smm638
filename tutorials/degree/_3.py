# !/usr/env/bin python3
#-*- encpding is utf-8 -*-

""""
--------------------------------------------------------------------------------
   Degree distribution plots with NetworkX
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk, credits to the Nx team
Dates:  - created
        - last change
Notes: This script illustrates two options to visualize the degree
       distribution of a network with Nx, namely a bar chart and a rank plot
"""

# %% load libraries
import collections
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# %% graph generator

# random graph
# --+ params
n, p = 100, 0.1
seed = 333
# --+ graph
G = nx.erdos_renyi_graph(n, p, seed=seed)

# get degree sequence
k = sorted([d for n, d in G.degree()], reverse=True)

# get count of nodes with degree 'k = k_i'
p_k = np.unique(k, return_counts=True)

# %% degree distribution plot - case A, barchart

# create figure
fig = plt.figure(figsize=(9, 6))

# create plot
ax = fig.add_subplot(1, 1, 1)

# plot data
plt.bar(p_k[0], p_k[1], width=0.80, color="b")

# aesthetics
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")

# draw graph in inset
plt.axes([0.125, 0.5, 0.3, 0.3])
pos = nx.spring_layout(G)
plt.axis("off")
nx.draw_networkx_nodes(G, pos, node_size=20)
nx.draw_networkx_edges(G, pos, alpha=0.4)
plt.show()

# %% degree distribution plot - case B, rank plot

# initialize a new figure and plot the data contestually
plt.loglog(k, "b-", marker="o")

# axes properties
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")

# draw graph in inset
plt.axes([0.15, 0.15, 0.4, 0.4])
Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
pos = nx.spring_layout(Gcc)
plt.axis("off")
nx.draw_networkx_nodes(Gcc, pos, node_size=20)
nx.draw_networkx_edges(Gcc, pos, alpha=0.4)
plt.show()
