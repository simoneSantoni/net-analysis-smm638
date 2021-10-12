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

# %%
# libraries
import networkx as nx
import numpy as np
import pandas as pd

# %%
# initialize a new nx graph class object
g = nx.Graph()

# %%
# add edges and nodes to the graph
nodes = [0, 1, 2, 3, 4]
edges = [(0, 1), (0, 2), (0, 3), (0, 4)]
g.add_nodes_from(nodes)
g.add_edges_from(edges)

# %%
# directed network
dg = nx.DiGraph()
nodes = [0, 1, 2]
edges = [(0, 1), (1, 0), (1, 2)]
dg.add_nodes_from(nodes)
dg.add_edges_from(edges)

# %%
wg = nx.Graph()
nodes = [0, 1, 2]
edges = [(0, 1, {"weight": 1, "year": 2021}),
         (0, 2, {"weight": 9, "year": 2020}),
         (1, 2, {'weight': 3, 'year': 2022})]
wg.add_nodes_from(nodes)
wg.add_edges_from(edges)

# %% 
# existing data
A = np.random.binomial(1, 0.1, size=(100, 100))
g = nx.from_numpy_array(A)

# %%
df = pd.DataFrame(A)
g = nx.from_pandas_adjacency(df)
# %%
