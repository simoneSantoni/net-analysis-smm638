# %% 
# module 
import matplotlib.pyplot as plt
import networkx as nx

# %% 
# indegree popularity 
g = nx.DiGraph()
g.add_nodes_from([0, 1, 2, 3, 4])
g.add_edges_from([(1, 0), (2, 0), (3, 0), (4, 0)])
pos = {0:(0, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1), 4:(-1, 0)}
fig = plt.figure(figsize=(2,2))
ax = fig.add_subplot(111)
nx.draw(g, pos=pos, ax=ax, with_labels=True, node_color="white")
plt.savefig("images/indegree_pop.pgf", bbox_inches="tight")
plt.show()

# %%
# outdegree popularity 
g = nx.DiGraph()
g.add_nodes_from([0, 1, 2, 3, 4])
g.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 4)])
pos = {0:(0, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1), 4:(-1, 0)}
fig = plt.figure(figsize=(2,2))
ax = fig.add_subplot(111)
nx.draw(g, pos=pos, ax=ax, with_labels=True, node_color="white")
plt.savefig("images/outdegree_pop.pgf", bbox_inches="tight")
plt.show()

# %%
# reciprocity
g = nx.DiGraph()
g.add_nodes_from([0, 1])
g.add_edges_from([(0, 1), (1, 0)])
pos = {0:(0, 0), 1:(1, 0)}
fig = plt.figure(figsize=(2,2))
ax = fig.add_subplot(111)
nx.draw(g, pos=pos, ax=ax, with_labels=True, node_color="white")
plt.savefig("images/reciprocity.pgf", bbox_inches="tight")
plt.show()

# %%
# triadic closure 
g = nx.DiGraph()
g.add_nodes_from([0, 1, 2])
g.add_edges_from([(0, 1), (1, 2), (0, 2)])
pos = {0:(0, 0), 1:(1, 1), 2:(2, 0)}
fig = plt.figure(figsize=(2,2))
ax = fig.add_subplot(111)
nx.draw(g, pos=pos, ax=ax, with_labels=True, node_color="white")
plt.savefig("images/triadic_closure.pgf", bbox_inches="tight")
plt.show()

# %%
# balance 
g = nx.DiGraph()
g.add_nodes_from([0, 1, 2, 3])
g.add_edges_from([(0, 2), (1, 2), (0, 3), (1, 3)])
pos = {0:(0, 0), 1:(2, 0), 2:(1, 1), 3:(1, 2)}
fig = plt.figure(figsize=(2,2))
ax = fig.add_subplot(111)
nx.draw(g, pos=pos, ax=ax, with_labels=True, node_color="white")
plt.savefig("images/balance.pgf", bbox_inches="tight")
plt.show()

# %%
# membership closure 
g = nx.DiGraph()
g.add_nodes_from([0, 1, "A", "B"])
g.add_edges_from([(0, "A"), (1, "B"), (0, 1)])
pos = {0:(0, 0), 1:(1, 0), "A":(0, 1), "B":(1, 1)}
fig = plt.figure(figsize=(2,2))
ax = fig.add_subplot(111)
nx.draw(g, pos=pos, ax=ax, with_labels=True, node_color="white")
g1 = nx.DiGraph()
g1.add_nodes_from([0, "B"])
g1.add_edges_from([(0, "B")])
pos = {0:(0, 0), "B":(1, 1)}
nx.draw(g1, pos=pos, ax=ax, with_labels=True, node_color="white", style="--")
plt.savefig("images/memberhip_closure.pgf", bbox_inches="tight")
plt.show()


# %%
# focal closure
g = nx.DiGraph()
g.add_nodes_from([0, 1, "A"])
g.add_edges_from([(0, "A"), (1, "A")])
pos = {0:(0, 0), 1:(2, 0), "A":(1, 1)}
fig = plt.figure(figsize=(2,2))
ax = fig.add_subplot(111)
nx.draw(g, pos=pos, ax=ax, with_labels=True, node_color="white")
g1 = nx.DiGraph()
g1.add_nodes_from([0,1])
g1.add_edges_from([(0, 1)])
pos = {0:(0, 0), 1:(2, 0)}
nx.draw(g1, pos=pos, ax=ax, with_labels=True, node_color="white", style="--")
plt.savefig("images/focal_closure.pgf", bbox_inches="tight")
plt.show()


# %%
