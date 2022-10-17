# %%
# load modules.
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import networkx as nx

# %%
# a star
fig = plt.figure(figsize=(2, 2))
ax = fig.add_subplot(111)
g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4, 5])
g.add_edges_from([(1, 3), (2, 3), (4, 3), (5, 3)])
pos = {1: (0, 0), 2: (0, 2), 3: (1, 1), 4: (2, 0), 5: (2, 2)}
nx.draw(g, pos=pos, node_color="white", edge_color="black", with_labels=True, ax=ax)
plt.savefig("images/star.pgf", bbox_inches="tight", pad_inches=0)

# %%
# a star
fig = plt.figure(figsize=(2, 2))
ax = fig.add_subplot(111)
g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4, 5])
g.add_edges_from([(1, 3), (2, 3), (4, 3), (5, 3), (1, 2), (1, 4), (2, 5), (4, 5)])
pos = {1: (0, 0), 2: (0, 2), 3: (1, 1), 4: (2, 0), 5: (2, 2)}
nx.draw(g, pos=pos, node_color="white", edge_color="black", with_labels=True, ax=ax)
plt.savefig("images/dense.pgf", bbox_inches="tight", pad_inches=0)

# %%
# clustering levels
fig = plt.figure(figsize=(1.5, 1.5))
ax = fig.add_subplot(111)
g = nx.Graph()
g.add_nodes_from(["ego", "a1", "a2", "a3"])
g.add_edges_from(
    [
        ("ego", "a1"),
        ("ego", "a2"),
        ("ego", "a3"),
        ("a1", "a2"),
        ("a1", "a3"),
        ("a2", "a3"),
    ]
)
pos = {"ego": (0, 0), "a1": (-1, 2), "a2": (0, 3), "a3": (1, 2)}
nx.draw(g, pos=pos, node_color="white", edge_color="black", with_labels=True, ax=ax)
plt.savefig("images/clustering_2.pgf", bbox_inches="tight", pad_inches=0)

# %%
# disconnected net
fig = plt.figure(figsize=(1.5, 1.5))
ax = fig.add_subplot(111)
g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
g.add_edges_from(
    [
        (1, 2),
        (3, 4),
        (4, 5),
        (3, 5),
    ]
)
pos = {1:(-1, 0), 2:(-1, 2), 3:(2, 1), 4:(4, -1), 5:(4, 3), 6:(7, 0), 7:(7, 1), 8:(7, 2)}
nx.draw(g, pos=pos, node_color="white", edge_color="black", with_labels=True, ax=ax)
plt.savefig("images/disconnected_net.pgf", bbox_inches="tight", pad_inches=0)

# %%
# a connected network
fig = plt.figure(figsize=(1.5, 1.5))
ax = fig.add_subplot(111)
g = nx.random_regular_graph(5, 8)
pos = nx.layout.circular_layout(g)
nx.draw(g, pos=pos, node_color="white", edge_color="black", with_labels=True, ax=ax)
plt.savefig("images/connected_net.pgf", bbox_inches="tight", pad_inches=0)
