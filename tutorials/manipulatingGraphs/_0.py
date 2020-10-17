
# !/usr/env/bin python3
#-*- encpding is utf-8 -*-

""""
--------------------------------------------------------------------------------
    IO operations with NewtworkX
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates: created Thu 31 Oct 14:29:59 2019
       last change Sun Nov 24 18:04:21 UTC 2019
Notes: This script reads the one-mode network dataset included in the
       'musae_ENGB_edges'
"""

# %% load libraries
import os
import numpy as np
import networkx as nx
import pandas as pd

# %% read dataset
"""
Notes on data format:

- the data included iin musae_ENGB_edges.csv are in the edgelist format;
- thus, each row is a an observed tie;
- the first element of the tuple is the 'from' node, while the second element is the 'to' node;
- the order of nodes is irrelevant as musae_ENGB_edges.csv reports frienship ties
"""

# path for the data file
os.getcwd()
in_file = os.path.join(os.getcwd(), 'data', 'musae_ENGB_edges.csv')
# read file
G = nx.read_edgelist(in_file,         # edgelist file to read
                     delimiter=',',   # delimiter between 'from' and 'to'
                     comments='#')    # the first line doesn't contain data

# %% write dataset in GraphML

"""
We see two different options:

- the GraphML is popular among network scientists; it's based on the XML
  format; this file format contains metadata on the network
- the adjancy list turns to be useful for graphs without data associated with
  nodes or edges and for nodes that can be meaningfully represented as
  strings
"""

# GrphML
# --+ path for the data file
out_file = os.path.join(os.getcwd(), 'data', 'to_graphml.xml')
# --+ write data
nx.write_graphml_xml(G, out_file)

# adjacency list
# --+ path for the data file
out_file = os.path.join(os.getcwd(), 'data', 'to_adjlist.adjlist')
# --+ write data
nx.write_adjlist(G, out_file)
