# !/usr/env/bin python3
#-*- encoding is utf-8 -*-

""""
--------------------------------------------------------------------------------
    Node centrality metrics
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates:  - created 17/10/2020, 23:05:11
        - last change 17/10/2020, 23:05:37
Notes: This script illustrates three popular centrality metrics, such as
       node degree, eigenvector centrality, and betweenness centrality
"""

# %% load libraries
import networkx as nx
from networkx.algorithms import degree_centrality
from networkx.algorithms import eigenvector_centrality
from networkx.algorithms import betweenness_centrality
import pandas as pd
import seaborn as sns

# %% visualization options
sns.set_theme(style="ticks")

# %% node centrality - case A, random graph

# generator
'''
a random graph can be generated using the Erdos-Renyi algorithm for example
'''
G = nx.erdos_renyi_graph(100, 0.1)

# draw network
nx.draw(G)

# degree
degree = degree_centrality(G)

# eigenvector_centrality
ec = eigenvector_centrality(G)

# betweeness centrality
bc = betweenness_centrality(G)

# visualize results
# --+ df
df = pd.DataFrame({'degree': degree, 'eigenvector_centrality': ec,
                   'betweenness_centrality': bc})
# --+ correlation matrix
df.corr()
# --+ scatter plot matrix
sns.pairplot(df)


# %% node centrality - case B, small world network

# generator
'''
a small world network can be simulated using the Watts-Strogatz algorithm
'''
G = nx.watts_strogatz_graph(100, 10, 0.1)

# draw network
nx.draw(G)

# degree
degree = degree_centrality(G)

# eigenvector_centrality
ec = eigenvector_centrality(G)

# betweeness centrality
bc = betweenness_centrality(G)

# visualize results
# --+ df
df = pd.DataFrame({'degree': degree, 'eigenvector_centrality': ec,
                   'betweenness_centrality': bc})
# --+ correlation matrix
df.corr()

# --+ scatter plot matrix
sns.pairplot(df)
