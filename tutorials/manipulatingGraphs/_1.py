# !/usr/env/bin python3
#-*- encpding is utf-8 -*-

""""
--------------------------------------------------------------------------------
    Convering to and from other formats
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates: created 17/10/2020, 23:05:11
       last change17/10/2020, 23:05:37
Notes: This script reads the one-mode network dataset included in the
       'musae_ENGB_edges'
"""

# %% load libraries
import os
import numpy as np
from scipy import io
import networkx as nx
import pandas as pd

# %% setup
wd = os.getcwd()

# %% network data as Pandas df

# source data
in_file = os.path.join(wd, 'data', 'musae_ENGB_edges.csv')
df = pd.read_csv(in_file, header=0, names=['v', 'u'])

# preview
df.head()

# let's assume the network is a weighted network
df.loc[:, 'weight'] = np.random.normal(loc=0, scale=1, size=len(df))

# %% from df to nx G
G = nx.from_pandas_edgelist(df,                # the df containing the data
                            source='u',        # first element of the dyad
                            target='v',        # second element of the dyad
                            edge_attr='weight')# weight

# %% from nx G to numpy/scipy

# numpy
a_np = nx.to_numpy_matrix(G)
# --+ let's write the data to a file using the .npy format
out_file = os.path.join(wd, 'data', 'from_numpy.npy')
np.save(out_file, a_np)
# scipy (more efficient)
a_sp = nx.to_scipy_sparse_matrix(G)
# --+ let's write the data to a file using the Matrix Market format
out_file = os.path.join(wd, 'data', 'from_scipy.mtx')
io.mmwrite(out_file, a_sp)
