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
k = 3
for community in itertools.islice(solutions, k):
    pp(list(sorted(c) for c in community))

# %% use the modularity index to appreciate the quality of alternative
#    paritioning solutions
# fit
solutions = girvan_newman(G)
# alternative paritioning solutions to consider
k = 10
# register modularity scores
modularity_scores = dict()
# iterate over solutions
for community in itertools.islice(solutions, k):
    solution = list(sorted(c) for c in community)
    score = modularity(G, solution)
    modularity_scores[len(solution)] = score
# plot modularity data
fig = plt.figure()
pos = list(modularity_scores.keys())
values = list(modularity_scores.values())
ax = fig.add_subplot(1, 1, 1)
ax.stem(pos, values)
ax.set_xticks(pos)
ax.set_xlabel(r'Number of communities detected')
ax.set_ylabel(r'Modularity score')
plt.show()
