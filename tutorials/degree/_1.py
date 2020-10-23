#!/usr/env/bin python3
# -*- encoding utf-8 -*-

""""
--------------------------------------------------------------------------------
    Degree distribution plots
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates:  - created 10/23/2020, 9:13:53 AM
        - last change 10/23/2020, 9:14:01 AM
Notes: This script illustrates three popular centrality metrics, such as
       node degree, eigenvector centrality, and betweenness centrality
"""

# %% Load libraries
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# %% Setup
plt.style.use('fivethirtyeight')

# %% Simulation

# random network
# --+ params
n, p = 5000, 0.05
seed = 333
# --+ graph
rn = nx.erdos_renyi_graph(n, p, seed=seed)
# small network
# --+ params
n, k, p = 5000, 5, 0.2
seed = 111

# graph
wsn = nx.watts_strogatz_graph(n, k, p, seed=seed)

# %% Random network degree distribution

# get nodal degree 'k' data as list
k_rn = sorted([d for n, d in rn.degree()], reverse=True)

# get 'p_k'
# --+ point-to-point probability
p_k = np.unique(k_rn, return_counts=True)
# --+ cumulative probability
cp_k = np.unique(k_rn, return_index=True)

# create figure
fig = plt.figure(figsize=(9, 4))

# add plot
ax0 = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)

# point-to-point data
# --+ plot data
ax0.scatter(p_k[0], p_k[1]/n, marker='o', color='black', alpha=0.4)
# --+ title
ax0.set_title("Point-to-point probability")
# --+ labels
ax0.set_ylabel("$Pr(k = k_{i})$")
ax0.set_xlabel("Degree $k$")

# cumulative probability
# --+ plot data
ax1.scatter(cp_k[0], cp_k[1]/n, marker='o', color='black', alpha=0.4)
# --+ title
ax1.set_title("Cumulative probability")
# --+ labels
ax1.set_ylabel("$Pr(k \geq k_{i})$")
ax1.set_xlabel("Degree $k$")

# show plot
plt.show()

# %% Small-world network

# get nodal degree 'k' data as list
k_wsn = sorted([d for n, d in wsn.degree()], reverse=True)

# get 'p_k'
p_k = np.unique(k_wsn, return_counts=True)
cp_k = np.unique(k_wsn, return_index=True)

p_k

# create figure
fig = plt.figure(figsize=(9, 4))

# add plot
ax0 = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)

# point-to-point data
# --+ plot data
ax0.scatter(p_k[0], p_k[1]/n, marker='o', color='black', alpha=1)
# --+ title
ax0.set_title("Point-to-point probability")
# --+ labels
ax0.set_ylabel("$Pr(k = k_{i})$")
ax0.set_xlabel("Degree $k$")

# cumulative probability
# --+ plot data
ax1.scatter(cp_k[0], cp_k[1]/n, marker='o', color='black', alpha=1)
# --+ title
ax1.set_title("Cumulative probability")
# --+ labels
ax1.set_ylabel("$Pr(k \geq k_{i})$")
ax1.set_xlabel("Degree $k$")

# show plot
plt.show()

# %% Random vs small world network degree distribution - rank plot

# create figure
fig = plt.figure(figsize=(6, 4))

# add plot
ax = fig.add_subplot(1, 1, 1)

# plot data with Matplotlib builtin 'loglog'
ax.loglog(k_wsn, marker='o', color='orange', alpha=0.4,
          label='Smalll world network')
ax.loglog(k_rn, marker='o', color='black', alpha=0.4,
          label='Random network')

# title
ax.set_title("Degree rank plot")

# labels
ax.set_ylabel(r"$k$")
ax.set_xlabel("Rank order")

# legend
ax.legend(loc="best")

# show plot
plt.show()
