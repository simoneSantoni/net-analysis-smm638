# !/usr/env/bin python3
# -*- encpding is utf-8 -*-

""""
--------------------------------------------------------------------------------
    Testing homophily in networks
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk

Dates: created Thu 31 Oct 14:29:59 2019
       last change Sun Nov 24 18:04:21 UTC 2019

Notes: This script tests the presence of homophily in a network. The setting is
       a one-mode, unweighted network reflecting friendship in the context of a
       postgraduate class. For sake of simplicity, we assume 'gender' is
       the only demographic attribute that shapes homophily.

"""


# %% load libraries
import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist

# %% style issues
plt.style.use('fivethirtyeight')

# %% simulate the observed network data
# seed
np.random.seed(000)
# nodes
n = 100
# proportion of female nodes
p = 0.5
# tie formation probabilities
p_ff = 0.25
p_mm = 0.20
p_fm = 0.01
# size of the sub-components of the adjacency
size=(int(n*p), int(n*p))
# let's assume the observed network exhibits sharp gender segregation
ff = np.random.binomial(1, p_ff, size=size)
mm = np.random.binomial(1, p_mm, size=size)
fm = np.random.binomial(1, p_fm, size=size)
mf = np.transpose(fm)
# the graph
g_left, g_right = np.vstack((ff, mf)), np.vstack((fm, mm))
g = np.hstack((g_left, g_right))
# fill diagonal values with 0s - we're not interested in the relationship
# a node has with itself
np.fill_diagonal(g, 0)
# count of female-female ties
c_ff = np.sum(ff)
# count of female-male or male-female ties
c_fm = 2 * np.sum(fm)
# count of male-male ties
c_mm = np.sum(mm)

# %% compare the focal network against 1,000 simulated networks
# define function
def assess_hompohily(_g,
                     _p,
                     _n,
                     _c_ff, _c_mm, _c_fm,
                     _n_iterations):
    '''
    :param _g: observed network (adjaceny matrix -- pass  a Numpy array)
    :param _p: proportion of gender = female nodes in the network
    :param _n: count of nodes in network
    :param _c_ff: count of female-female ties in the observed network
    :param _c_mm: count of male-male ties in the observed network
    :param _c_fm: count of female - male ties in the observed network
    :param _n_iterations: count
    :return: list of cosine similarity scores along with descriptive
             statistics
    '''
    # fix seed
    np.random.seed(000)
    # containers
    # --+ count ties by type (homophilous Vs heterophilous)
    _r_ff, _r_fm, _r_mm = 0, 0, 0
    # --+ distance between observed and simulated data
    _dist = []
    # iterate over simulated distribution of genders
    for iteration in range(_n_iterations):
        # --+ reshuffling the gender of nodes; gender = female is coded as 1
        _reshuffled = np.random.binomial(1, p, size=n)
        # --+ iterate over each dyad in g
        for i in range(n):
            for j in range(n):
                # --+ sample the tie in the network
                t = [g[i][j]][0]
                # --+ if tie is present, evaluate whether it's a homphilous or
                # --- heterophilous tie based on the reshuffled network
                if t == 1:
                    h = np.sum([_reshuffled[i], _reshuffled[j]])
                    if h == 2:
                        _r_ff += 1
                    elif h == 1:
                        _r_fm += 1
                    elif h == 0:
                        _r_mm += 1
                    else:
                        pass
                else:
                    pass
        # get the distance between the observed and simulated distribution
        # of ties with respect to three following categories: (i)
        # female-female; (ii) female-male; (iii) male-male. Scipy doc is the
        # place start to get a closer understanding of `cosine similarity'
        # as a distance metric (see scipy.spatial.distance).
        _observed = np.array([c_ff, c_fm, c_mm])
        _simulated = np.array([_r_ff, _r_fm, _r_mm])
        to_append = pdist([_observed, _simulated], metric='cosine')
        _dist.append(to_append[0])
    # return statistics on the distance between the observed and siimulated
    # distributions of ties with respect to type (homophilopus Vs.
    # heterophilous)
    # --+
    _mean, _std, _min, _max = np.mean(_dist), np.std(_dist),\
                              np.min(_dist), np.max(_dist)
    print(80 * '-',
          'Descriptive statistics on observed-simulated ' \
          'distances',
          80 * '-',
          'Mean: %s' % np.round(_mean, 2),
          'Std. dev.: %s' % np.round(_std, 2),
          'Min: %s' % np.round(_min, 2),
          'Max: %s' % np.round(_max, 2),
          end='\n',
          sep='\n')
    # --+ plot the distribution of sum of squares
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(_dist,
            bins=50, cumulative=False, density=False,
            color='orange', alpha=0.5,
            histtype='bar')
    ax.set_xlabel(r'Cosine similarity')
    ax.set_ylabel(r'Count of simulation runs')
    ax.set_title(r'Exploring homophily in graph G')
    # --+ save figure
    plt.tight_layout()
    plt.savefig('cosine_sim_distr.pdf')
    # --+ return objects
    return(_dist, [_mean, _std, _min, _max])


# %% deploy function
outcome = assess_hompohily(_g=g, _p=p, _n=n,
                           _c_mm=c_mm, _c_ff=c_ff, _c_fm=c_fm,
                           _n_iterations=1000)

# %% save results
# --+ individual data points (N = 1,000)
with open('cosine_sim_scores.pickle', 'wb') as pipe:
    pickle.dump(outcome[0], pipe)
# --+ save mean, std, min, max
with open('cosine_sim_stats.pickle', 'wb') as pipe:
    pickle.dump(outcome[1], pipe)
