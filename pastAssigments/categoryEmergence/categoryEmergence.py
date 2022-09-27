# %% Libraries
# --+ utils
import os, glob, json, warnings, itertools
# --+ suppress warnings
warnings.simplefilter("ignore") 
# --+ core libraries
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from graspologic.plot import heatmap
from sklearn.metrics.pairwise import cosine_similarity

# %% Data
# --+ params
CWD = os.getcwd()
FOLDER = 'c4p'
# --+ get files path
files = [file for file in glob.glob(os.path.join(CWD, FOLDER, '*.csv')) if 'c4p_thread_list' not in file]
# --+ load
df = pd.concat((pd.read_csv(file) for file in files), axis=1)
# --+ clean
df.drop(columns=['Unnamed: 0'], inplace=True)
df = df.loc[:,~df.columns.duplicated()]
# --+ info
df.info()

# %% Node
# --+ filter
df_ev = df[df['on_electric'] == 1].copy()
# --+ parse lists
columns = ['sentiment', 'subjectivity']
for column in columns:
	df_ev[column] = df_ev[column].apply(json.loads)
# --+ node characteristics
authors_ev = df_ev.explode(columns).groupby('author', as_index=False)['sentiment', 'subjectivity'].aggregate(np.mean)

# %% Threads and edges
# --+ threads
threads = list(set(df_ev.id.to_list()))
# --+ edges
edges = list(set(df_ev.loc[:,['id', 'author']].to_records(index=False).tolist()))

# %% Bi-partite and projection
# --+ empthy graph
bg = nx.Graph()
# --+ add nodes
nodes = authors_ev['author'].to_list()
bg.add_nodes_from(nodes, bipartite=0)
bg.add_nodes_from(threads, bipartite=1)
# --+ get nx object
bg.add_edges_from(edges)
# --+ check
print(
	"""
Is bipartite? {}
	""".format(nx.is_bipartite(bg))
) 
# --+ project
g_n = nx.bipartite.projected_graph(bg, nodes)

# %% Graph
# --+ basic plot
fig = plt.figure(figsize=(6, 6))
pos = nx.spring_layout(g_n)
nx.draw_networkx(g_n, 
		pos=pos, 
		node_size=50, 
		with_labels=False)
plt.axis("off")

# %% Node-level tasks
# --+ pass nodes attributes
for node, se, su in zip(authors_ev.author, authors_ev.sentiment, authors_ev.subjectivity):
	g_n.nodes[node]["avg_se"] = se
	g_n.nodes[node]["avg_su"] = su
# --+ isolates
isolates = list(nx.isolates(g_n))
g_i  = g_n.subgraph(isolates)
avg_se_i = list(nx.get_node_attributes(g_i, "avg_se").values())
avg_su_i = list(nx.get_node_attributes(g_i, "avg_su").values())
# --+ print info
print(
	"""
All sample descriptive:

{}

Number of Isolates: {}

	Sentiment [-1.0, +1.0]
	- avg_se: {} 
	- min_se: {}
	- max_se: {}

	Subjectivity [0.0, 1.0]
	- avg_su: {}
	- min_su: {}
	- max_su: {}
""".format(authors_ev.describe(),
	len(isolates), 
	np.mean(avg_se_i), 
	min(avg_se_i), 
	max(avg_se_i), 
	np.mean(avg_su_i), 
	min(avg_su_i), 
	max(avg_su_i))
)
# --+ get connected
connected = g_n.nodes - isolates
g_c = g_n.subgraph(connected)
# --+ connected
print(
	"""
Number of connected components: {}
	""".format(nx.algorithms.number_connected_components(g_c))
)

# %% Descriptive analysis
# --+ hist
n_bins = 20
node_degree = [degree for node, degree in nx.degree(g_c)]
fig, ax = plt.subplots(tight_layout=True)
ax.hist(node_degree, bins=n_bins)
ax.set_xlabel('Degree (k)')
ax.set_ylabel('Frequency')
plt.show()

# --+ hist cumulative
node_degree = [degree for node, degree in nx.degree(g_c)]
fig, ax = plt.subplots(tight_layout=True)
ax.hist(node_degree, density=True, cumulative=1, bins=n_bins)
ax.set_xlabel('Degree (k)')
ax.set_ylabel('Cumulative p')
plt.show()

# --+ dictionary
d = {
	# --+ degree centrality
	"degree" : nx.algorithms.degree_centrality(g_c),
	# --+ betweenness centrality
	"betweenness" : nx.algorithms.betweenness_centrality(g_c),
	# --+ eigenvector centrality
	"eigenvector" : nx.algorithms.eigenvector_centrality(g_c),
	}
# --+ pass to pandas
df_c = pd.DataFrame(d)
# --+ get descriptive
print(df_c.describe())
# --+ pairplot
ax = pd.plotting.scatter_matrix(df_c, figsize=(6,6), range_padding=0.15)
ax[0,0].set_yticks([5, 25, 50, 75, 100])
ax[0,0].set_yticklabels([0.00, 0.15, 0.30, 0.45, 0.60])
plt.show()


# %% Core-periphery
# --+ heatmap
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
heatmap(g_c, cmap='coolwarm', ax=ax, sort_nodes=True, cbar=False) 

# %% Explore communities
# --+ fit
solutions = nx.algorithms.community.girvan_newman(g_c)
# alternative paritioning solutions to consider
k = 19
# register modularity scores
modularity_scores = dict()
# iterate over solutions
for community in itertools.islice(solutions, k):
    solution = list(sorted(c) for c in community)
    score = nx.algorithms.community.modularity(g_c, solution)
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
# %% Explore "optimal" k
# --+ fit
solutions = nx.algorithms.community.girvan_newman(g_c)
# alternative paritioning solutions to consider
k = 12
# register modularity scores
modularity_scores = dict()
# iterate over solutions
for community in itertools.islice(solutions, k):
    solution = list(sorted(c) for c in community)
# let's check the solution
for community in solution:
	print(len(community)) # number of nodes in the community
# %% Similarity
# --+ compute
similarity = {}
for u, v in g_c.edges():
    key = "{}-{}".format(u, v)
    u_att = [[g_c.nodes[u]["avg_se"], g_c.nodes[u]["avg_su"]] ]
    v_att = [[g_c.nodes[v]["avg_se"], g_c.nodes[v]["avg_su"]] ]
    value = cosine_similarity(u_att, v_att)
    similarity[key] = value
# --+ get some descriptive
df = pd.DataFrame([i[0][0] for k, i in similarity.items()])
df.describe()

# %% Set positions
# --+ position connected nodes
pos_c = nx.spring_layout(g_c)
# --= position isolates
pos_i = {}
x = 0
for i in g_i.nodes:
	pos_i.update({i: (0, x)})
	x = x+1

# %% Get attributes
# --+ get sentiment
c_se = list(nx.get_node_attributes(g_c,'avg_se').values())
i_se = list(nx.get_node_attributes(g_i,'avg_se').values())
# --+ get subjectivity
c_su = list(nx.get_node_attributes(g_c,'avg_su').values())
i_su = list(nx.get_node_attributes(g_i,'avg_su').values())

# %% Sentiment graph
# --+ figure
fig = plt.figure(figsize=(12, 12))
# --+ set up partitions
gs = gridspec.GridSpec(1, 6,
                       figure=fig)
# --+ add plots
ax_0 = fig.add_subplot(gs[0, 0:4]) 
ax_1 = fig.add_subplot(gs[0, 4:5]) 
# --+ connected graph
nx.draw_networkx(g_c, 
		pos=pos_c, 
		with_labels=False, 
		node_color=c_se,
		vmin=min(c_se),
		vmax=max(c_se), 
		node_size=100,
		edge_color='w',
		width=0.05, 
		cmap="coolwarm",
		ax=ax_0)
# --+ isolates graph
nx.draw_networkx(g_i, 
		pos=pos_i, 
		with_labels=False, 
		node_color=i_se,
		vmin=min(i_se),
		vmax=max(i_se), 
		node_size=100,
		edge_color='w',
		width=0.05, 
		cmap="coolwarm",
		ax=ax_1)
# --+ axis
ax_0.axis('off')
ax_1.axis("off")
# --+ plot
plt.show()

# %% Subjectivity plot
# --+ figure
fig = plt.figure(figsize=(12, 12))
# --+ set up partitions
gs = gridspec.GridSpec(1, 6,
                       figure=fig)
# --+ add plots
ax_0 = fig.add_subplot(gs[0, 0:4]) 
ax_1 = fig.add_subplot(gs[0, 4:5]) 
# --+ connected graph
nx.draw_networkx(g_c, 
		pos=pos_c, 
		with_labels=False, 
		node_color=c_su, 
		vmin=min(c_su),
		vmax=max(c_su),
		node_size=100,
		edge_color='w',
		width=0.05, 
		cmap="coolwarm",
		ax=ax_0)
# --+ isolates graph
nx.draw_networkx(g_i, 
		pos=pos_i, 
		with_labels=False, 
		node_color=i_su, 
		vmin=min(i_su),
		vmax=max(i_su),
		node_size=100,
		edge_color='w',
		width=0.05, 
		cmap="coolwarm",
		ax=ax_1)
# --+ axis
ax_0.axis('off')
ax_1.axis("off")
# --+ plot
plt.show()

# %% Sentiment and Subjectivity plot
# --+ figure
fig = plt.figure(figsize=(12, 12))
# --+ set up partitions
gs = gridspec.GridSpec(1, 6,
                       figure=fig)
# --+ add plots
ax_0 = fig.add_subplot(gs[0, 0:4]) 
ax_1 = fig.add_subplot(gs[0, 4:5]) 
# --+ connected graph 
nx.draw_networkx(g_c, 
		pos=pos_c, 
		with_labels=False, 
		node_color=c_se, # blue (negative) to red (positive)
		vmin=min(c_se),
		vmax=max(c_se), 
		node_size=1/np.array(c_su)*5, # reversed (objectivity larger)
		edge_color='w',
		width=0.05, 
		cmap="coolwarm",
		ax=ax_0)
# --+ isolates graph 
nx.draw_networkx(g_i, 
		pos=pos_i, 
		with_labels=False, 
		node_color=i_se, # blue (negative) to red (positive)
		vmin=min(i_se),
		vmax=max(i_se), 
		node_size=1/np.array(i_su)*5, # reversed (objectivity larger)
		edge_color='w',
		width=0.05, 
		cmap="coolwarm",
		ax=ax_1)
# --+ axis
ax_0.axis('off')
ax_1.axis("off")
# --+ plot
plt.show()

# %% Let's get a peripheral
author = 'Woodster'
print(
	"""
	Name: {}

	Centrality:
		- Degree: {}
		- Betweenness: {}
		- Eigenvector: {}
	
	Post content:
	
		"{}"

	""".format(author, 
		df_c[df_c.index == author].degree[0],
		df_c[df_c.index == author].betweenness[0],
		df_c[df_c.index == author].eigenvector[0],
		[i for i in df_ev[df_ev['author'] == author].content][0][10:35].replace('\\', ''))
)

# %% Managerial recomandation
print(
	"""
As a community manager interested in promoting positive attitudes towards
electric vehicles, you may want to

	- help disconnected peripheral nodes with positive sentiment to
	engage more:
		* Why opinionated nodes are interesting?
	
	- persuade confused central nodes

How would you implement this?
	"""
)