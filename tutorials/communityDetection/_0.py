# !/usr/env/bin python3
#-*- encoding is utf-8 -*-

""""
--------------------------------------------------------------------------------
    Node centrality metrics
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates:  - created 10/25/2020, 11:45:30 PM
        - last change
Notes:  This script shows how to:
        - fit the Girvman-Newman algorithm with NetworkX
        - assess the validity of alternative paritioning solutions
"""

# %% load libraries
import itertools
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community import girvan_newman, modularity
from pprint import pprint as pp

# %% sample data

# load the karate club graph
G = nx.karate_club_graph()

# %% inspect the networkx

# basic info
pp(nx.info(G))

# draw the network
pos = nx.spring_layout(G)
nx.draw(G, pos, alpha=1, node_color='white')
nx.draw_networkx_labels(G, pos)
plt.axis("off")
plt.show()

# %% fit Girvman-Newman algorithm on the Karate Club dataset

# retrieve the two community-solution
# --+ fit
solutions = girvan_newman(G)
# --+ display node2community affiliations
tuple(sorted(c) for c in next(solutions))

# retrieve the first 'k' community-solution
# --+ fit
solutions = girvan_newman(G)
# --+ display node2community affiliations
k = 2
for community in itertools.islice(solutions, k):
    pp(list(sorted(c) for c in community))

# %% use the modularity index to appreciate the quality of alternative
#    paritioning solutions

# sample data
G = nx.barbell_graph(3, 0)

# fit
solutions = girvan_newman(G)

# empty list to record modularity scores
modularity_scores = []

for solution in solutions:
    for community in solution:
        to_evaluate.append(community)
        pp(to_evaluate)


# %% on going
#first compute the best partitiona
partition = community_louvain.best_partition(G)

# compute the best partition
partition = community_louvain.best_partition(G)

# draw the graph
pos = nx.spring_layout(G)
# color the nodes according to their partition
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()

# %%



nx.draw(G)
