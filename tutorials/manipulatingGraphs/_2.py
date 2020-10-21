# !/usr/env/bin python3
#-*- encpding is utf-8 -*-

""""
--------------------------------------------------------------------------------
    Iterating over nodes and edges
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates: created 10/21/2020, 8:11:57 AM
       last change
Notes: This script reads the one-mode network dataset included in the
       'musae_ENGB_edges'
"""

# %% overview of methods (unditrected, unweighted graph)

"""
Graph.__init__([incoming_graph_data])
    → Initialize a graph with edges, name, or graph attributes.

Graph.add_node(node_for_adding, **attr)
    → Add a single node node_for_adding and update node attributes.

Graph.add_nodes_from(nodes_for_adding, **attr)
    → Add multiple nodes.

Graph.remove_node(n)
    → Remove node n.

Graph.remove_nodes_from(nodes)
    → Remove multiple nodes.

Graph.add_edge(u_of_edge, v_of_edge, **attr)
    → Add an edge between u and v.

Graph.add_edges_from(ebunch_to_add, **attr)
    → Add all the edges in ebunch_to_add.

Graph.add_weighted_edges_from(ebunch_to_add)
    → Add weighted edges in ebunch_to_add with specified weight attr

Graph.remove_edge(u, v)
    → Remove the edge between u and v.

Graph.remove_edges_from(ebunch)
    → Remove all edges specified in ebunch.

Graph.update([edges, nodes])
    → Update the graph using nodes/edges/graphs as input.

Graph.clear()
    → Remove all nodes and edges from the graph.

Graph.clear_edges()
    → Remove all edges from the graph without altering nodes.
"""

# %% load libraries
import os
import networkx as nx
from pprint import pprint as pp

# %% setup
wd = os.getcwd()

# %% load network dataset
in_file = os.path.join(wd, 'data', 'musae_ENGB_edges.csv')
G = nx.read_edgelist(in_file, delimiter=',', comments='#')    # the first line doesn't contain data

# %% iterating over nodes
V = G.nodes()

list(V)[0:5]

# degree method
G.degree('6194')

# %% iterating over edges
E = G.edges()

list(E)[0:5]

# focal's neighbors
G['6194']
G.adj['6194']

# querying edges based on v
list(G.edges(['6194', '255']))

# getting neighbors for multiple, target focals
focals = ['6194', '255']
neighbors = [[focal, list(G.adj[focal])] for focal in focals]

neighbors

# iterating with the adjacency method
[(focal, neighbors) for focal, neighbors in G.adjacency()]
