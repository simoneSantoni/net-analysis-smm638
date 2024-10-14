# %%
# load modules.
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import networkx as nx
import pandas as pd

# %% literature citing

# @article{white1976social,
#   title={Social structure from multiple networks. I. Blockmodels of roles
#          and positions},
#   author={White, Harrison C and Boorman, Scott A and Breiger, Ronald L},
#   journal={American journal of sociology},
#   volume={81},
#   number={4},
#   pages={730--780},
#   year={1976},
#   publisher={University of Chicago Press}
# }

# read data
df = pd.read_csv("citing_white_et_al.csv")

# commont outlets
journals = pd.DataFrame(df.groupby(["Source title"]).size())
journals.rename(columns={0: "count"}, inplace=True)
journals.reset_index(inplace=True)  
journals.sort_values("count", ascending=False, inplace=True)
journals[0:50]
journals.loc[journals["Source title"].str.contains("Sociolog")][0:50]
# most cited articles
df.sort_values("Cited by", ascending=False, inplace=True)
df.loc[df["Cited by"].notnull(), ["Source title", "Authors", "Title", "Cited by"]][0:50]

# %% QAP
from numpy.random import default_rng
from scipy.optimize import quadratic_assignment
rng = default_rng()
n = 15
A = rng.random((n, n))
B = rng.random((n, n))
res = quadratic_assignment(A, B)  # FAQ is default method
print(res.fun)

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
pos = {
    1: (-1, 0),
    2: (-1, 2),
    3: (2, 1),
    4: (4, -1),
    5: (4, 3),
    6: (7, 0),
    7: (7, 1),
    8: (7, 2),
}
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

# %%
# random network
fig = plt.figure(figsize=(2.5, 2.25))
ax = fig.add_subplot(111)
ax.set_facecolor("white")
g = nx.random_regular_graph(5, 100)
pos = nx.layout.spring_layout(g)
nx.draw(
    g,
    pos=pos,
    node_color="k",
    edge_color="k",
    node_size=2,
    alpha=0.3,
    width=0.5,
    with_labels=False,
    ax=ax,
)
plt.savefig("images/random_net.pgf", bbox_inches="tight", pad_inches=0)

# %%
# small-world network
fig = plt.figure(figsize=(2.5, 2.25))
ax = fig.add_subplot(111)
ax.set_facecolor("white")
g = nx.watts_strogatz_graph(100, 10, 0.02)
pos = nx.layout.kamada_kawai_layout(g)
nx.draw(
    g,
    pos=pos,
    node_color="k",
    edge_color="k",
    node_size=2,
    alpha=0.3,
    width=0.5,
    with_labels=False,
    ax=ax,
)
plt.savefig("images/small_world.pgf", bbox_inches="tight", pad_inches=0)


# %%
