# load networkx
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from collections import Counter

# intialize a 1-mode, undirected, unweighted network
g1 = nx.Graph()
g2 = nx.Graph()

# populate the two networks
## limited clustering case
g1.add_nodes_from(np.arange(0, 10, 1))
g1.add_edges_from(
    [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9)]
)
g1.add_edge(5, 9)
g1.add_edge(5, 4)
nx.draw(g1, with_labels=True, node_color="w")

## more clustering case
g2 = nx.complete_graph(10)
nx.draw(g2, with_labels=True, node_color="orange")

# compute clustering
g1_clustering = nx.clustering(g1)
g2_clustering = nx.clustering(g2)

## visual comparison
g1_clustering_dist = Counter(g1_clustering)
g2_clustering_dist = Counter(g2_clustering)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(g1_clustering_dist.keys(), g1_clustering_dist.values(), label="Almost a star")
plt.show()