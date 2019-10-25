#!/usr/env/bin python3

"""
########################################################
#                                                      #
#                DEGREE DISTRIBUTION                   #
#                                                      #
########################################################

Author: Simone Santoni

Created on: Sat  21 Sun 06:23:46 UTC 2018

Revised on: Sat  8 Dec 07:27:49 UTC 2018

Notes: this is the first of a series of tutorials on NA

"""


# this is a stupid comment

#%% setup

import os
import networkx as nx
import matplotlib.pyplot as plt


#%% read data

"""
In this example, I'm reading the user-projection
of the user-forum affiliation network.
"""

path = '/Users/simone/Desktop/net-analysis-smm638'
folder = 'tutorials/data'
in_f = 'user_user_graph.csv'

target = os.path.join(path, folder, in_f)

g = nx.read_edgelist(open(target, 'rb'))


#%% make plot of simple degree distribution

degree_sequence = sorted([d for n, d in g.degree()], reverse=True)  # degree
# sequence


# print "Degree sequence", degree_sequence

dmax = max(degree_sequence)


# plot the data

plt.loglog(degree_sequence, marker='o', color='b')
plt.title("Degree rank plot")
plt.ylabel("Degree (unweighted network)")
plt.xlabel("Rank")

# draw graph in inset

plt.axes([0.2, 0.2, 0.4, 0.4])


gcc = sorted(nx.connected_component_subgraphs(g), key=len, reverse=True)[0]
pos = nx.spring_layout(gcc)
plt.axis('off')
nx.draw_networkx_nodes(
        gcc, pos, node_size=10, node_color='r', alpha=0.10
        )
nx.draw_networkx_edges(
        gcc, pos, alpha=0.01
        )

# show the plot

plt.show()

