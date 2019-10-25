# Tutorial #0 - README

This tutorial deals with three main network analytic tasks:

+ computing/visualizing the degree distribution of a network
+ manipulating two-mode (i.e., bipartite) networks
+ computing centrality of individual nodes (i.e., how well-connected an
 actor/entity is in the network is)[1]
 
 The folder `data` contains two network datasets concerning an online
  community of beer enthusiasts:
  
+ `user_user_graph.csv` contains a one-mode network linking the members
    of the community who interact with each other (i.e., individuals `i` 
    and `j` chatting in the forum);
+ `all_user_interaction.csv` contains a two-mode network connecting the
    members of the community with certain events (e.g., individual `i` 
    posting a review on product `j`; individual `i` subscribes 
    to forum `j`).

These data files are organized as edge lists. Each line is a tie linking
two nodes `i` and `j`. The first column reports node `i`, the second column reports node
`j`. Optionally, edge attributes can be included (e.g., a timestamp telling us
when the `i-j` tie emerged).

Storing network data in edge lists is more efficient than storing data in 
adjacency matrices. In very simple terms, edge lists report only the 1-s
included in an adjacency matrix.

The scripts included in this tutorial show how to read edge lists in `Networkx`
using the functions `read_edge_list` and `from_pandas_edgelist`.


 ---
 Notes:
 
 [1] The topic of centrality will be further discussed over the second part
  of the module. 

