# !/usr/bin/env python3
# -*- encoding utf-8 -*-

"""
-------------------------------------------------------------------------------
    Kossinets - Watts model
-------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Date: created ; last change
Notes:
    - data consist of email exchange events collected by the SNAP crowd
    - location: https://snap.stanford.edu/data/email-Eu-core-temporal.html
    - site: data come from a large European research institution. Here's a quote
      from the SNAP website: "We have anonymized information about all incoming
      and outgoing email between members of the research institution. The
      e-mails only represent communication between institution members (the
      core), and the dataset does not contain incoming messages from or outgoing
      messages to the rest of the world. A directed edge (u, v, t) means that
      person u sent an e-mail to person v at time t. A separate edge is created
      for each recipient of the e-mail. We also have four sub-networks
      corresponding to the communication between members of four different
      departments at the institution. Node IDs in the sub-networks do not
      correspond to the same node ID in the entire network."
"""


# %% load modules
import os
import pandas as pd
import numpy as np


# %% load data
"""
I specify the location of the file by means of the 'os' module.
Particularly, I use 'os.path.join' in order to join 'path',
'folder', and 'file name' elements. Note os.path.join should be
imported.
If you run this, update your path and folder strings.
"""

cwd = os.getcwd()
fdr = 'tutorials/_2'
in_f = 'email-Eu-core-temporal.txt'
df = pd.read_table(os.path.join(cwd, fdr, in_f),
                   sep=' ',
                   header=None,
                   names=['src', 'tgt', 'ts'])


# %% clean time data
"""
The place to start is, as usual, data cleaning. Specifically, we want to
create a variable capturing the time elapsed since the first email
exchanged by network participants. In order to do this, we leverage the
amazing capabilities Pandas has to deal with 'time' data.
Please go back to the 'Timeseries'/'Timedeltas' sections of the Pandas
documentation.
"""

# fix the timespan for the analysis (in days)
timespan = 30

# time elapsed since the first email
df.loc[:, 'td'] = pd.to_timedelta(df['ts'], unit='s')
df.loc[:, 'm'] = df['td'].dt.days // timespan


# %% get unique nodes
"""
We will use the set of unique nodes to get the set of ties that are at risk
to emerge in every period (or 'timedelta' to use Pandas' terminology).
"""

# sources
n = list(set(df['src']))

# targets
n.extend(list(set(df['tgt'])))

# collapse sources and targets
n = list(set(n))

# get a data frame whose index is constant and equal to zero
n = pd.DataFrame({'n': n}, index=np.repeat(0, len(n)))


# %% get unique timespans
"""
Related to the previous point, we need the set of unique periods.
"""

# unique months
m = list(set(df['m']))

# filter-in those email exchange occurring before 19 months since the
# first interaction
m = [i for i in m if i < 19]

# get a data frame whose index is constant and equal to zero
m = pd.DataFrame({'m': m}, index=np.repeat(0, len(m)))


# %% get the risk set of ties to emerge in each timespan
"""
Since we have the set of unique nodes and the set of unique periods stored in
memory, we get the set of ties that are at risk to emerge in every period.
In algebraic terms, this is equivalent to the Cartesian Product of two
vectors. There are several ways to achieve the Cartesian Product in Python:
    - naive, Panda-based implementation
    - numpy.meshgrid
    - ad-hoc solutions implemented in numpy (e.g.,
      https://gist.github.com/hernamesbarbara/)
    - itertools (https://docs.python.org/3/library/itertools.html)
Stackoverflow has a useful thread focusing on how to operate a Cartesian
Product in Python (https://stackoverflow.com/questions/1208118/using-numpy
-to-build-an-array-of-all-combinations-of-two-arrays)
In our case, we will go for the naive implementation with Pandas (which is
very efficient indeed; you can verify by applying the %timeit magic over
alternative pieces of code implementing the Cartesian Product.
"""


# node-node cartesian product
rs = pd.merge(n, n, left_index=True, right_index=True)

# risk set-timespan cartesian product
rs = pd.merge(rs, m, left_index=True, right_index=True)

# focus on the lower triangle of the adj matrix
rs = rs.loc[rs['n_x'] < rs['n_y']]


"""
If you go with numpy.meshgrid, the code is:
nodes = n['n'].values.tolist()
rs = pd.DataFrame(np.stack(np.meshgrid(nodes, nodes)).T.reshape(-1, 2),
                  columns=['n_x', 'n_y'])
Let me highlight the logic:
    - we create a list out of the 'n' columns in the 'n' df
    - we apply meshgrid
    - we stack the output of np.meshgrid (namely, two arrays of shape
      (len(n), len(n))
    - we transpose the stacked arrays by means of the .T function
    - we reshape so as the get an array of shape (len(n**2), 2)
    - we create a Pandas df out of the np array
If you wan to go with itertools, you can go for itertools.product. Snippets of
code are available here:
https://docs.python.org/3/library/itertools.html#itertools.product
That said, I don't recommend to go down this route. The underlying coding
philosophy is a bit old school -- not particularly efficient. No offense for
'loop' lovers.
"""


# %% group email exchange data around unique src-tgt-td
"""
The first transformation procedure to apply is grouping observations around
unique source-target-period instances. The main goal here is to avoid
duplicates. See also  next comment on this.
"""

# group by
gr = df.groupby(['src', 'tgt', 'm'], as_index=False)
df.loc[:, 'ml_cnt'] = 1
df = pd.DataFrame(gr['ml_cnt'].agg(np.size))


# %% nest src-tgt within unique dyads
"""
As per the Kossinets-Watts model, a tie emerges between two nodes i, j insofar
as i sends an email to j and j sends an email to i (say j
replies/reciprocates to i's email message). So, we have to disentangle data
ties and potentiallt asymmetric email exchange.
The 'trick' is to nest email exchange data within ties by means of the 'set'
function. This us allows to get rid of the order in which pairs of nodes can
present. E.g.: set([0,1]) == set([1, 0]) gives 'True'
During the second extra-lab, you guys proposed to use the 'set' function to
create a new column within the data frame containing actual ties. That seems
an appeal alternative but it doesn't work as it comes to manipulate the column
containing sets (e.g., to assign sets to the index of the dataframe.
The reason is that set objects are not mutable and cannot be hashed
(meaning you can't get the i-th element of the set).
The following lines of code show how to properly leverage 'sets' in the
context of our problem (that is, nesting email exchange observations into
ties). Here's the logic:
- we create two empty lists to separately store the nodes involved in
  individual pairs of ties (say focal and alter nodes).
- we iterate over the columns of the Pandas dataframe to compose sets out of
  'src' and 'tgt' entities, namely senders and recipients
- we pick-up the individual elements of sets (it is possible to do that
  as sets have been transformed into lists, which are hashable).
- we add the vectors containing set elements to the Pandas data frame.
"""

focal, alter = [], []

for i, j in zip(df['src'], df['tgt']):
    dyad = list(set([i, j]))
    focal.append(dyad[0])
    alter.append(dyad[1])


df.loc[:, 'n_x'] = focal
df.loc[:, 'n_y'] = alter

del (focal, alter)


# %% locate actual ties by month
"""
We assess the presence of a tie by counting the observations nested within
unique triplets of 'n_x', 'n_y', 'm' (this is what np.count_nonzero
accomplishes). If the count is greater than 1 it means both src-tgt and
tgt-src are present within a certain set and period.
Once we have located the ties we proceed by slicing the Pandas data frame so
as to filter-out the instances in which A sends an email to B while B doesn't
reciprocate.
Note the count is dimished by '1' as this makes the interpretation of the
column easier.
"""

gr = df.groupby(['n_x', 'n_y', 'm'])
df.loc[:, 'tie'] = 1
df.loc[:, 'tie'] = gr['tie'].transform(np.count_nonzero) - 1
df = df.loc[df['tie'] == 1]


# %% cumulate ties over 'n_x' - 'n_y' pairs
"""
At this point, we want to take into account the fact that
information exchange ties don't disappear: If i and j are connected
in period 0 they will remain connected up to time k, it doesn't
matter if they exchance or not exchange emails.
Here, we index the data on ties around unique pairs of nodes. Then we sort
ties with respect to their emergence. Finally, we count the ties (cum_tie)
involving a same pair of nodes over time.
"""

df.set_index(['n_x', 'n_y', 'm'], inplace=True)
df.sort_index(inplace=True)
gr = df.groupby(level=['n_x', 'n_y', 'm'])
ct = pd.DataFrame(gr['tie'].aggregate(np.max))
gr = ct.groupby(level=['n_x', 'n_y'])
ct = pd.DataFrame(gr['tie'].aggregate(np.cumsum))
ct.rename(columns={'tie': 'cum_ties'}, inplace=True)


# %% merge data on actual and potential ties
"""
Now, we're ready to merge data on actual and potential ties.
"""

# reset the index of the data frame
ct.reset_index(inplace=True)

# merge data on actual and potential ties
g = pd.merge(rs, ct, on=['n_x', 'n_y', 'm'], how='left')

# replace NaNs
g.loc[g['cum_ties'].isnull(), 'cum_ties'] = 0

# create categorical variable
g.loc[:, 'tie'] = 0
g.loc[g['cum_ties'] > 0, 'tie'] = 1


# %% attach data on alters
"""
For each tie (being an actual or potential one) and period we want to
retrieve the set of alters developed by each node from time 0
up to the focal period.
In order to do this, we may want to:
    - iterate over each 'src' and 'm' combination
    - get the list of alters
"""

# src and periods over which to iterate
nodes = n['n'].values.tolist()
months = m['m'].values.tolist()

# list to populate
alr = []

# reset indices
df.reset_index(inplace=True)

# for loop
for i in nodes:
    for j in months:
        to_append = df.loc[(df['src'] == i) & (df['m'] <= j),
                           'tgt'].values.tolist()
        to_append = list(set(to_append))
        alr.append([i, j, to_append])

# get a df out of the list
alr = pd.DataFrame(alr, columns=['n', 'm', 'alr'])


# %% merge actual/potential ties with alters
"""
It's time to attach each node's alters to each individual
pair so as to get 'k', namely the number of contacts i and j share
"""

# let's start with n_x
alr.loc[:, 'n_x'] = alr['n']
g = pd.merge(g, alr[['n_x', 'm', 'alr']], on=['n_x', 'm'], how='left')
g.rename(columns={'alr': 'n_x_alr'}, inplace=True)

# let's do the same with n_y
alr.loc[:, 'n_y'] = alr['n']
g = pd.merge(g, alr[['n_y', 'm', 'alr']], on=['n_y', 'm'], how='left')
g.rename(columns={'alr': 'n_y_alr'}, inplace=True)


# %% compute k
"""
We can get k as the intersection between 'n_x_alr' and
'n_y_alr'. In Python, we can achieve this in several ways:
    - leveraging sets
        * list(set(a) & set(b))
        or
        * set(a).intersection(b)
    - using np.intersect1d
    - creating ad-hoc functions
      (e.g., https://www.geeksforgeeks.org/python-intersection-two-lists/)
In order to make the comparison faster/more efficient, we may want to remove
those instances in which a least one node in the pair doesn't have any
connection
"""


# we're iterating over the g data frame, which contains 8,740,890 observations
# in the interest of efficiency we should be better off using a list
# comprehension

# shared alters
shared_alters = [list(set(g.loc[i, 'n_x_alr']) & set(g.loc[i, 'n_y_alr'])) for i in g.index]

# count of shared alters
k = [len(i) for i in shared_alters]

# get a data frame
k = pd.DataFrame({'shared_alters': shared_alters, 'k': k}, index=g.index)

# append data on actual and potential ties and k
g = pd.concat([g, k], axis=1)

# drop redundant cols
g.drop(['n_x_alr', 'n_y_alr'], axis=1, inplace=True)

# set and sort data
g.set_index(['n_x', 'n_y', 'm'], inplace=True)
g.sort_index(inplace=True)

# adjust cum_ties field
g.loc[g['cum_ties'] > 0, 'tie'] = 1
g.loc[:, 'cum_ties'] = g.groupby(level=['n_x', 'n_y'])['tie'].transform(np.cumsum)

# housekeeping - remove redundant col
g.drop('shared_alters', axis=1, inplace=True)


# %% get T(k)
"""
At this point, we have to assess the probability that, conditionally on k,
pairs of unconnected nodes will link in the 'following' period. This implies:
    - we distinguish among connected and unconnected pairs of nodes
    - we locate the period in which two previously unconnected ties become
      connected
    - get the proportions of 'triads' that close because of the existence
      of k shared contacts
"""

# get the lag of 'tie' within pairs
g.loc[:, 'tie_lag'] = g.groupby(level=['n_x', 'n_y'])['tie'].shift()
g.loc[g['tie_lag'].isnull(), 'tie_lag'] = 0

# locate tie formation events
g.loc[:, 'tie_frm'] = 0
select = (g['cum_ties'] == 1) & (g['tie_lag'] == 0) & (g['tie'] == 1)
g.loc[select, 'tie_frm'] = 1

# filter-out pairs of connected nodes
g = g.loc[(g['tie'] == 0) | (g['tie_frm'] == 1)]

# aggregate data around k-m pairs
g.reset_index(inplace=True)
g.loc[:, 'tie_cnt'] = 1
t = g.groupby(['k', 'm'], as_index=False)[['tie_frm', 'tie_cnt']].agg(np.sum)

# get T(k)
t.loc[:, 'tk'] = t['tie_frm'] / t['tie_cnt']

# housekeeping
t = t.loc[t['m'] <= 16]

# export
t.to_csv('tk.csv', index=False)


# %% plot T(k)
"""
Uncomment if you want to run.
The visualization strategy should keep into account that pairs of nodes are
very heterogeneously distributed across k. This might make t(k) extremely
sensitive as k increases. So, first-thing-first, explore the
distribution of pairs across k. Then, fix an appropriate range of variation
for k. Finally, make the visualization of t(k) over k.
Three main insights arise from the visualization:
    1 - the functional form of T(k) is contingent on time
    2 - no matter the functional form, the average T(K) changes markedly
        as time passes
    3 - given 1) and 2), results from triadic closure models would be
        properly contextualized (how mature is the network? How many prior
        ties? Do newcomers join the network? ...
"""

## setup
#import matplotlib.pyplot as plt
#import matplotlib as mpl
#plt.style.use('seaborn-bright')
#import pandas as pd
#import numpy as np
#
#
## read data
#df = pd.read_csv('tk.csv')
#
## explore the distribution of pairs over k
#df.groupby(['k', 'm'])['tie_cnt'].aggregate(np.sum)
#
#"""
#There seems to be a knot in the distribution around k = 15. Let's stick
#with that (and slice the data).
#"""
#
#df = df.loc[df['k'] <= 15]
#
## create figure
#fig = plt.figure(figsize=(6, 4))
#
## create chart
#ax = fig.add_subplot(1, 1, 1)
#
## colors for individual lines
#n = 16 # months we focus on
#c = np.arange(0, n, 1)
#cmap = mpl.cm.get_cmap('viridis', n)
#
## plot the data
#for i in np.arange(0, 16, 1):
#    k = df.loc[df['m'] == i, 'k']
#    tk = df.loc[df['m'] == i, 'tk']
#    # label = str(i)
#    ax.plot(k, tk, c=cmap(i)) # label=label)
#
#
## axes
#ax.set_xlabel('$k$')
#ax.set_ylabel('$T(k)$')
#
## grid
#ax.grid(True, ls='--')
#
## colorbar
#d = ax.scatter(c, c, marker='', c=c, cmap=cmap)
#fig.colorbar(d)
#
## legend
## ax.legend(loc='best')
#
## show the plot
#plt.show()
