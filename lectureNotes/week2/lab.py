# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
------------------------------------------------------------------------------
   lab.py    |    familiairze with key classes, methods, and functions
             |    inluded in the NetworkX package
------------------------------------------------------------------------------

Author   : Simone Santoni, simone.santoni.1@city.ac.uk

Synopsis : This script covers the following points

           - familiarizing with the NetworkX library
           - initializing a NetworkX Graph object
           - one-mode network
           - undirected, unweighted network
           - directed, unweighted network
           - undirected, weighted network
           - directed, weighted network
           - two mode network
           - testing the network is bipartite
           - initializing a NetworkX Graph object using diverse Python objects
           - ... NumPy
           - ... Pandas
           - ... lists
           - ... SciPy
           - iterating over a graph's vertices and edge
           - computing node centrality indicators (e.g., degree)
           - computing the average degree of a network
           - computing the degree distribution of a network
 
Status   : frozen

"""

# %% libraries
import collections
import networkx as nx
import numpy as np
import scipy as sp
import scipy.sparse
import matplotlib.pyplot as plt
import pandas as pd

# %% undirected network
# initialize an NX object of class Graph
from networkx.algorithms import bipartite

g = nx.Graph()
# add nodes intand edges to the graph
nodes = [0, 1, 2, 3, 4]
edges = [(0, 1), (0, 2), (0, 3), (0, 4)]
g.add_nodes_from(nodes)
g.add_edges_from(edges)

# %% directed network
# initialize an NX object of class DiGraph
dg = nx.DiGraph()
# add nodes and edges to the graph
nodes = [0, 1, 2]
edges = [(0, 1), (1, 0), (1, 2)]
dg.add_nodes_from(nodes)
dg.add_edges_from(edges)

# %% undirected, weighted network
'''
basically, there's nothing special to do in NX, which doesn't have a class 
for weighted graphs
''' 
# initialize an NX object of class Graph
wg = nx.Graph()
# add nodes and edges to the graph
nodes = [0, 1, 2]
# weights are edge attributes (you can pass whatever attribute you want)
edges = [(0, 1, {"weight": 1, "year": 2021}),
         (0, 2, {"weight": 9, "year": 2020}),
         (1, 2, {'weight': 3, 'year': 2022})]
wg.add_nodes_from(nodes)
wg.add_edges_from(edges)

# %% directed, weighted network
'''
basically, there's nothing special to do in NX, which doesn't have a class 
for weighted graphs
''' 
# initialize an NX object of class DiGraph
wdg = nx.DiGraph()
# add nodes and edges to the graph
nodes = [0, 1, 2]
# weights are edge attributes (you can pass whatever attribute you want)
edges = [(0, 1, {"weight": 1, "year": 2021}),
         (1, 0, {"weight": 9, "year": 2020}),
         (2, 0, {'weight': 3, 'year': 2022})]
wg.add_nodes_from(nodes)
wg.add_edges_from(edges)

# %% two-mode network (also known as bipartite graphs)
'''
basically, there's nothing special to do in NX, which doesn't have a class 
for bipartite graphs
'''
# initialize an NX object of class DiGraph
bg = nx.Graph()
# add nodes and edges to the graph
bottom_nodes = ['a', 'b', 'c']
top_nodes = [0, 1, 2]
egdes = [('a', 0), ('a', 1), ('b', 1), ('c', 2)]
bg.add_nodes_from(bottom_nodes, bipartite=0)
bg.add_nodes_from(top_nodes, bipartite=1)
bg.add_edges_from(edges)
# check the graph is bipartite
nx.algorithms.bipartite.is_bipartite(bg)

bg = nx.Graph()
bottom_nodes = ['a', 'b', 'c', 'd']
top_nodes = ['x', 'y', 'z']
bg.add_nodes_from(bottom_nodes, bipartite=0)
bg.add_nodes_from(top_nodes, bipartite=1)
edgelist = [('a', 'x'), ('a', 'y'), ('b', 'y'), ('c', 'z'), ('d', 'x')]
bg.add_edges_from(edgelist)

nx.algorithms.bipartite.is_bipartite(bg)

# %% initializing a graph from existing objects
# NumPy object
A = np.random.binomial(1, 0.1, size=(100, 100))
g = nx.from_numpy_array(A)
# from edgelist
edge_list = [(0, 1), (0, 2), (0, 3), (0, 4)]
g = nx.from_edgelist(edge_list)
# from SciPy parse
A = sp.sparse.eye(2, 2, 1)
g = nx.from_scipy_sparse_matrix(A)
# Pandas object
df = pd.DataFrame(A)
g = nx.from_pandas_adjacency(df)

# %% iterating over a graph's vertices and edge
# generate a random graph
g = nx.generators.erdos_renyi_graph(n=100, p=0.1)
# get nodes
g.nodes()
# get edgelist
g.edges()

# %% computing node centrality indicators (e.g., degree)
g.degree()

# %% computing the average degree of a network
dv = dict(g.degree())
k = list(dv.values())
print("""
==============================================
    Summary stats on degree distribution
==============================================

Mu    :       {:.3f}

Min   :       {:>5}
Max   :       {:>5}


Sigma :       {:.3f}

""".format(np.mean(k), np.min(k), np.max(k), np.std(k)))

# %% computing the degree distribution of a network
ds = collections.Counter(k)
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(1, 1, 1)
ax.scatter(ds.keys(), ds.values(), color='k')
ax.set_xlabel('Degree')
ax.set_ylabel('Counts of nodes')
plt.show()
