# !/usr/env/bin python3
#-*- encpding is utf-8 -*-

""""
--------------------------------------------------------------------------------
    Projection of two-mode networks
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates: created 10/21/2020, 8:11:57 AM
       last change
Notes: This script reads transforms a two-mode network (e.g., a person-to-team
       affiliation network) into two one-mode networks (a person-person
       network - in which individuals are connected when they belong to the same
       team - and team-team network - in which individuals are connected when
       they share at least a member)
"""


#%% load libraries
import numpy as np
import networkx as nx
from networkx.algorithms import bipartite as bp
import pandas as pd
from os import getcwd
from os.path import join
import progressbar
from time import sleep


#%% read data
path = '/home/simone/Dropbox/teaching'
folder = 'smm638/finalCourseProject/dataPackage'
f = 'all_user_interactions.csv'

df = pd.read_csv(join(path, folder, f))


#%% clean

# drop housekeeping column

df.drop('call', axis=1, inplace=True)


# rename cols

old_cols = ['Unnamed: 0', 'value']
new_cols = ['id', 'event']
df.rename(columns=dict(zip(old_cols, new_cols)), inplace=True)


# slice for forums

"""
let's assume `forums' are the type of events we
want to focus on for the social net part
"""

df = df.loc[df['var'] == 'forum']
df = df.loc[df['var'].notnull()]
df.drop('var', axis=1, inplace=True)


# get forum 'id'

df.loc[:, 'event'] = df['event'].str.split('forums/').str.get(1)
df.loc[:, 'event'] = df['event'].str.strip('/')
df = df.loc[df['event'].notnull()]


# cleaning usr column

df.loc[:, 'usr'] = df['usr'].str.split(
        '.').str.get(1).str.strip('/')


# create a bipartite network with nX

top_nodes = set(df['event'])
bottom_nodes = set(df['usr'])


# get nx object

b = nx.from_pandas_edgelist(df, source='usr', target='event')


# `is bipartite` check

is_bip = nx.is_bipartite(b)


# getting network projections

print("Start projecting 2-mode network data")
bar = progressbar.ProgressBar(
    maxval=5,
    widgets=[progressbar.Bar('>', '[', ']'),' ', progressbar.Percentage()]
)
bar.start()


# get the unweighted projections of the two-mode networks

gu = bp.projected_graph(b, bottom_nodes)
ge = bp.projected_graph(b, top_nodes)


# get the weighted projections of the two-mode networks

"""
The weighted projected graph is the projection of the bipartite
network B onto the specified nodes with weights representing
the number of shared neighbors or the ratio between actual
shared neighbors and possible shared neighbors if ratio is
True. The nodes retain their attributes and are connected
in the resulting graph if they have an edge to a common node
in the original graph.
"""

gu_w = bp.weighted_projected_graph(b, bottom_nodes, ratio=True)
ge_w = bp.weighted_projected_graph(b, top_nodes, ratio=True)


bar.finish()
print("Done!")


# write projections and node labels to files

path = '/home/simone/Dropbox/teaching'
folder = 'smm638/finalCourseProject/dataPackage'

f0 = 'event_event_graph.csv'
nx.write_edgelist(ge, open(join(path, folder, f0), 'wb'))


f1 = 'user_user_graph.csv'
nx.write_edgelist(gu, open(join(path, folder, f1), 'wb'))

f2 = 'event_event_weighted_graph.csv'
nx.write_weighted_edgelist(ge_w, open(join(path, folder, f2), 'wb'))

f3 = 'user_user_weighted_graph.csv'
nx.write_weighted_edgelist(gu_w, open(join(path, folder, f3), 'wb'))

f4 =  'bipartite_graph.csv'
nx.write_edgelist(b, open(join(path, folder, f4), 'wb'))


#%% SCRIPT ENDS HERE
