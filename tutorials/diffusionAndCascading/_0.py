# !/usr/env/bin python3
#-*- encpding is utf-8 -*-

""""
--------------------------------------------------------------------------------
   Implementing Easley and Kleinberg's diffusion model
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk

Dates:  - created
        - last change

Notes:

"""

# %% import libraries
import numpy as np
import networkx as nx
from pprint import pprint as pp

# %% initialize network
'''
We initialize the network reported in Figure 19.3 of Easley and Kleienberg's
book (page 503)
'''
# the new graph
g = nx.Graph()
# nodes
nodes = ['v', 'r', 's', 'w', 't', 'u']
# edges
edges = [('v', 'r'), ('v', 'w'), ('v', 't'), ('r', 's'), ('r', 'w'),
         ('w', 't'), ('w', 'u'), ('w', 's'), ('s', 'u'), ('t', 'u')]
# populate the graph
g.add_nodes_from(nodes)
g.add_edges_from(edges)
# visualize graph
pos = nx.layout.kamada_kawai_layout(g)
nx.draw(g, node_color='w', pos=pos, with_labels=True)

# %% initialize the diffusione process
# parameters
# --+ pay-off of adopting the new behavior
a = 1
# --+ pay-off of the status quo (not changing)
b = 1
# get degree 'd'
degree = nx.degree(g)
# initial state
# --+ the list of adopters is empty
adopters = []
# --+ everybody sticks with the status quo
#     let's create a node-level attribute reflecting adoption
for node in g.nodes:
    g.nodes[node]["adopting"] = 0
# ----+ double-check attributes
#pp(g.nodes.data())

# %% model the diffusion process
# at time 1 there are early adopters emerge for some reasons
# --+ new adopters
early_adopters = ['w']
# --+ expand the set of adopters
adopters.extend(early_adopters)
# --+ adopt node attributes
for adopter in adopters:
    g.nodes[adopter]['adopting'] = 1
# draw the network
colors = []
for n in g.nodes():
    if g.nodes[n]['adopting'] == 1:
        colors.append('orange')
    else:
        colors.append('white')
nx.draw(g, pos=pos, with_labels=True, node_color=colors)

# %% let's simulate what happens in the following periods as nodes make decisions
for focal in nodes:
    # count adopting neighbors
    focal_nbrs = list(g.neighbors(focal))
    p = np.sum([g.nodes[nbr]['adopting'] for nbr in focal_nbrs])
    # pay-off of adopting new behavior
    d = g.degree(focal)
    a_payoff = p * a
    b_payoff = (d - p ) * b
    # decision to adopt
    if (g.nodes[focal]['adopting'] == 0) & (a_payoff > b_payoff):
        g.nodes[focal]['adopting'] = 1
        adopters.extend(focal)
    else:
        pass
# outcome of the cascading behavior
adopters

# %% draw the network
colors = []
for n in g.nodes():
    if g.nodes[n]['adopting'] == 1:
        colors.append('orange')
    else:
        colors.append('white')
nx.draw(g, pos=pos, with_labels=True, node_color=colors)
