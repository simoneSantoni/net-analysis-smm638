#!/usr/env/bin python3
#-*- encoding utf-8 -*-


'''
=======================
Description of the task
-----------------------

Use NumPy to simulate a 1-mode, unweighted, and undirected network
with 1000 nodes. This synthetic network should have the following
degree distribution:

k  | p(k)
---|-----
0  | 0
1  | 0.1
2  | 0.35
3  | 0.25
4  | 0.1
5  | 0.1
6  | 0.04
7  | 0.01
8  | 0.02
9  | 0.02
10 | 0.01
'''

# %% load library
import numpy as np
import networkx as nx

# %% characteristics of the network
N = 1000
nodes = np.arange(0, N, 1)
p_k = [0.1, 0.35, 0.25, 0.1, 0.1, 0.04, 0.01, 0.02, 0.02, 0.01]
k = np.arange(1, 11, 1)

# %% simulate degree sequence
d = dict(zip(nodes, np.random.choice(k, p=p_k, replace=True, size=N)))

# %%

# simulate the left-hand sife of an edge list
adj = []
for node in nodes:
    items = list(np.repeat(node, d[node]))
    adj.extend(items)

np.random.shuffle(adj)


while len(adj) > 0:
    # --+ start from a focal node that we randomly draw
    focal = adj[0]
    # --+ avoid to sample self loops
    adj = [i for i in adj if i != focal]
    # --+ sample alters
    keys = np.random.choice(adj, size=d[focal], replace=False)
    alters = [adj[key] for key in keys]
    # --+ remove sampled edges from the risk set
    for key in keys:
        adj.remove(key)
    # --+ update degree sequence
    for alter in alters:
        d[alter] = d[alter] - 1

#TODO: to complete and test!
