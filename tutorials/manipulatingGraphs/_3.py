# !/usr/env/bin python3
#-*- encpding is utf-8 -*-

""""
--------------------------------------------------------------------------------
    Projection of two-mode networks
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates: created 10/21/2020, 8:11:57 AM
       last change
Notes: This script reads transforms a two-mode network (e.g., a person-to-team
       affiliation network) into two one-mode networks (a person-person
       network - in which individuals are connected when they belong to the same
       team - and team-team network - in which individuals are connected when
       they share at least a member)
"""


#%% load libraries
import numpy as np
import networkx as nx
from networkx.algorithms import bipartite as bp
import pandas as pd

#%% fake data
'''
We simulate an incidence matrix with 100 mode-1/bottom nodes (e.g.,
individuals) and  10 mode-2/top nodes (e.g., products).
'''
# numpy simulation
n, k = 100, 10
bottom_nodes = np.arange(0, n)
top_nodes = np.arange(n, n+k)
edges = []
for i in bottom_nodes:
    # random number of ties from a poisson distribution
    degree = np.random.poisson(lam=3, size=1)
    # alters
    alters = np.random.choice(top_nodes, size=degree)
    # add edges
    for alter in alters:
        edges.append((i, alter))


|#%% graph creation
# empthy graph
bg = nx.Graph()
# add nodes
bg.add_nodes_from(bottom_nodes, bipartite=0)
bg.add_nodes_from(top_nodes, bipartite=1)
# get nx object
bg.add_edges_from(edges)
# `is bipartite` check
is_bip = nx.is_bipartite(bg)

# %% getting network projections
# get the unweighted projections of the two-mode networks
g_b = bp.projected_graph(bg, bottom_nodes)
g_t = bp.projected_graph(bg, top_nodes)
# get the weighted projections of the two-mode networks
"""
The weighted projected graph is the projection of the bipartite
network B onto the specified nodes with weights representing
the number of shared neighbors or the ratio between actual
shared neighbors and possible shared neighbors if ratio is
True. The nodes retain their attributes and are connected
in the resulting graph if they have an edge to a common node
in the original graph.
"""
g_b_w = bp.weighted_projected_graph(bg, bottom_nodes, ratio=True)
g_t_w = bp.weighted_projected_graph(bg, top_nodes, ratio=True)

# %% write projections and node labels to files
path = 'data'
folder = 'bipartiteGraph'
f0 = 'event_event_graph.csv'
nx.write_edgelist(ge, open(join(path, folder, f0), 'wb'))
f1 = 'user_user_graph.csv'
nx.write_edgelist(gu, open(join(path, folder, f1), 'wb'))
f2 = 'event_event_weighted_graph.csv'
nx.write_weighted_edgelist(ge_w, open(join(path, folder, f2), 'wb'))
f3 = 'user_user_weighted_graph.csv'
nx.write_weighted_edgelist(gu_w, open(join(path, folder, f3), 'wb'))
f4 =  'bipartite_graph.csv'
nx.write_edgelist(b, open(join(path, folder, f4), 'wb'))
