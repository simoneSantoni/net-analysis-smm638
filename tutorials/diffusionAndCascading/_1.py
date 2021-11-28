# !/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
------------------------------------------------------------------------------
    _1.py    |    assessing dyadic similarity in node attributes (e.g., 
             |    preferences)
------------------------------------------------------------------------------

Main steps of the tutorial:

1 - import libraries

2 - simulate a network (200 nodes)

3 - simulate node attibutes (1 attribute, A)

4 – plot data to emphasize node attibutes

5 – assess dydic similarity

"""

# %% 1 - libraries
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# %% 2 - simulate a network
n = 200
G = nx.connected_watts_strogatz_graph(n, k=2, p=0.7)

# %% 3 - simulate node attributes
A = np.random.randint(100, size=n)
for node, a in zip(G.nodes, A):
    G.nodes[node]["attr"] = a

# %% 4 - network visualization
fig = plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, node_color=A, cmap="coolwarm")
nx.draw_networkx_labels(G, pos=pos)
plt.axis("off")

# %% 5 - appreciating dyadic similarity
similarity = {}
for u, v in G.edges():
    key = "{}-{}".format(u, v)
    value = np.abs(G.nodes[u]["attr"] - G.nodes[v]["attr"])
    similarity[key] = value