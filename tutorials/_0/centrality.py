#!/usr/bin/python3

"""
###################################################
#                                                 #
#         CENTRALITY INDICATORS IN nX             #
#                                                 #
###################################################


Author: Simone Santoni, simone.santoni.1@city.ac.uk

Created on: Sat  27 Oct 05:14:06 UTC 2018

Revised on: Sat  8 Dec 07:27:49 UTC 2018

Notes:

    - none
"""


#%% setup

import os

from os import getcwd
from os.path import join
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import collections


#%% read data

"""
In this example, I'm reading the user-projection
of the user-forum affiliation network.

Note, the networkI'm reading is weighted, so I  read
use read_weighted_edgelist function
"""

path = '/home/simone/Dropbox/teaching/smm638'
folder = 'finalCourseProject/dataPackage'
f = 'user_user_weighted_graph.csv'

g = nx.read_weighted_edgelist(
        open(join(path, folder, f), 'rb'),
        delimiter=' '
        )

# double-check edges attributes for a sample edge

"""
optional run:

 In[ ]: g.edges['738632', '822751']
Out[ ]: {'weight': 0.019230769230769232}
"""


#%% betweeness

bw = nx.betweenness_centrality(g, weight='weight')


#%% eigenvector centrality

"""
The eigenvector centrality indicator is a refined version
of nodal degree that takes into account the centrality
of contacts, such that the more central are a node's alters
the higher its eigenvector centrality.all

The key reference -- presented in class -- is:

Phillip Bonacich. “Power and Centrality: A Family of Measures.”
American Journal of Sociology 92(5):1170–1182

Note the eigenvector centrality indicator comes in two flavors:
    - pure Python
    - Numpy implementation (faster)
"""

eg = nx.eigenvector_centrality_numpy(g, weight='weight')

#%% SCRIPT ENDS HERE
