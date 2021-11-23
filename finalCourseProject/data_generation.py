# %% libraries
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# %% key figures
# number of nodes
n = 192

# %% trading floor layout
# desk size
desk = 16
# x-values
x_values = [1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 21, 22]
x = []
for i in x_values:
    a = np.repeat(i, desk)
    x.extend(a)
# y-values
y_values = np.arange(0, desk)
y = np.tile(y_values, int(n / desk))
# bind values together
pos_layout = {}
for i in range(n):
    pos_layout[i] = np.array([x[i], y[i]])

# %% knowledge transfer network
G = nx.watts_strogatz_graph(n=n, k=4, p=0.25)

# %% visualization
# draw the knowledge transfer network
pos = nx.spring_layout(G)
nx.draw(G, pos, alpha=1, node_color="white")
nx.draw_networkx_labels(G, pos)
plt.axis("off")
plt.show()
# project the knowledge transfer network on the layout
nx.draw(G, pos_layout, alpha=1, node_color="white")
nx.draw_networkx_labels(G, pos_layout)
plt.axis("off")
plt.show()

# %% add node preference for ai
# create attitudes toward ai
ai = np.random.poisson(lam=5, size=n)
for i in range(len(ai)):
    if ai[i] > 10:
        ai[i] = 10
    elif ai[i] == 0:
        ai[i] = 1
    else:
        pass
# pass attitudes to the network
for node, attr in zip(G.nodes, ai):
    G.nodes[node]["ai"] = attr
    
# %% pass location data
for node, i, j in zip(G.nodes, x, y):
        G.nodes[node]["x_pos"] = i
        G.nodes[node]["y_pos"] = j

# %% create network autocorrelation
# sample nodes
sample_nodes = np.random.choice(G.nodes, 20)
# update attributes
for node in sample_nodes:
    # focal attitude toward ai
    focal = G.nodes[node]["ai"]
    # get alters
    alters = list(G.adj[node])
    # alterate attitudes toward ai
    for alter in alters:
        new = focal + np.random.choice([-2, -1, 0, 1, 2])
        if new > 10:
            new = 10
        elif new < 0:
            new = 0
        else:
            pass
        G.nodes[alter]["ai"] = new

# %% draw the knowledge transfer network
# get colors
ai = []
for node in G.nodes():
    ai.append(11 - G.nodes[node]["ai"])
for i in range(len(ai)):
    if ai[i] > 10:
        ai[i] = 10
    elif ai[i] == 0:
        ai[i] = 1
    else:
        pass       

# %% draw the knowledge transfer network
pos = nx.spring_layout(G)
nx.draw(G, pos, alpha=1, cmap=plt.get_cmap("coolwarm"), node_color=ai)
nx.draw_networkx_labels(G, pos)
plt.axis("off")
plt.show()
# project the knowledge transfer network on the layout
nx.draw(G, pos_layout, alpha=1, cmap=plt.get_cmap("coolwarm"), node_color=ai)
nx.draw_networkx_labels(G, pos_layout)
plt.axis("off")
plt.show()

# %% write data
nx.write_graphml_xml(G, 'trading_floor.xml')
