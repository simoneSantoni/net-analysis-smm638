# %%
# import
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# %%
# a sparse graph

# the graph
g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(9, 10)
# node positions
pos = {
    1: (0, 0),
    2: (1, 0),
    3: (0, 1),
    4: (1, 1),
    5: (2, 1),
    6: (0, 2),
    7: (1, 2),
    8: (2, 2),
    9: (0, 3),
    10: (1, 3),
}
# draw network
fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111)
options = {"node_color": "white", "edge_color": "black", "node_size": 500}
nx.draw(g, with_labels=True, **options, ax=ax, pos=pos)
plt.savefig("images/sparse_graph.pgf", bbox_inches="tight", backend="pgf")

# %%
# dense network

# the graph
g = nx.random_regular_graph(6, 10, seed=99)
# node positions
pos = nx.spring_layout(g, k=0.5, iterations=5000)
# draw network
fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111)
options = {"node_color": "white", "edge_color": "black", "node_size": 500}
nx.draw(g, with_labels=True, **options, ax=ax, pos=pos, connectionstyle="arc3, rad=1")
plt.savefig("images/dense_graph.pgf", bbox_inches="tight", backend="pgf")


# %%
# expected profitability
x = np.linspace(0, 1, 100)
y = -1 + x - x**2
fig = plt.figure(figsize=(2.75, 2.75))
ax = fig.add_subplot(111)
ax.plot(x, y, color="black")
ax.hlines(y=-0.85, xmin=0, xmax=1, color="grey", linestyles="dashed")
ax.text(1.05, -0.855, "$\Pi = 0$")
ax.hlines(y=-1, xmin=0, xmax=1, color="red", linestyles="dashed")
ax.text(-0.15, -1.005, "$-\delta$")
ax.set_xlabel("$\phi$")
ax.set_ylabel("$E(\Pi)$")
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.spines["left"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
plt.savefig("images/expected_profitability.pgf", bbox_inches="tight", backend="pgf")

# %%
# buyer seller network
fig = plt.figure(figsize=(3, 2))
ax = fig.add_subplot(111)
g = nx.Graph()
g.add_nodes_from(["b1", "b2", "b3"])
g.add_nodes_from(["s1", "s2", "s3", "s4"])
g.add_edge("s1", "s2")
g.add_edge("s1", "s3")
# g.add_edge("s2", "s3")
pos = {
    "b1": (0, 0),
    "b2": (0, 1),
    "b3": (0, 2),
    "s1": (3, 1),
    "s2": (2, 2),
    "s3": (4, 2),
    "s4": (3, 0),
}
nx.draw(g, pos=pos, node_color="white", with_labels=True, ax=ax)
ax.text(-0.5, 2.5, "Buyers", fontsize=13)
ax.text(2.5, 2.5, "Sellers", fontsize=13)
plt.savefig("images/buyer_seller_network.pgf", bbox_inches="tight", backend="pgf")
# %%
