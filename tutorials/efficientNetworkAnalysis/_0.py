{
"cells": [
{
"cell_type": "markdown",
"metadata": {},
"source": [
"# Setup"
]
},
{
"cell_type": "code",
"execution_count": 1,
"metadata": {},
"outputs": [],
"source": [
"from graph_tool.all import *"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"# Why Graph-tool?\n",
"\n",
"+ NetworkX is perfect for prototyping - it's flexible and provides a variety of algorithms and functions\n",
"+ Graph-tool complements NetworkX - it makes possible to scale a prototype up (see the [performance comparison results](https://graph-tool.skewed.de/performance))"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"# Manipulating graphs"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## Creating a graph"
]
},
{
"cell_type": "code",
"execution_count": 14,
"metadata": {},
"outputs": [],
"source": [
"# by default, new graphs are directed\n",
"g = Graph()\n",
"\n",
"# if you want an undirected graphs\n",
"ug = Graph(directed=False)"
]
},
{
"cell_type": "code",
"execution_count": 15,
"metadata": {},
"outputs": [],
"source": [
"# to force a graph to be undirected\n",
"assert ug.is_directed() == False"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## Adding vertices and edges linking vertices"
]
},
{
"cell_type": "code",
"execution_count": 18,
"metadata": {},
"outputs": [],
"source": [
"# adding vertices one-by-one\n",
"v1 = g.add_vertex()\n",
"v2 = g.add_vertex()"
]
},
{
"cell_type": "code",
"execution_count": 19,
"metadata": {},
"outputs": [],
"source": [
"# adding multiple vertices in a row\n",
"vlist = g.add_vertex(2)"
]
},
{
"cell_type": "code",
"execution_count": null,
"metadata": {},
"outputs": [],
"source": [
"# edges\n",
"e = g.add_edge(v1, v2)"
]
},
{
"cell_type": "code",
"execution_count": 17,
"metadata": {},
"outputs": [
{
"name": "stdout",
"output_type": "stream",
"text": [
"0 1\n"
]
}
],
"source": [
"# calling edges\n",
"print(e.source(), e.target())"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## Iterating over vertices and edges"
]
},
{
"cell_type": "code",
"execution_count": 22,
"metadata": {},
"outputs": [
{
"name": "stdout",
"output_type": "stream",
"text": [
"0\n",
"1\n",
"2\n",
"3\n",
"4\n",
"5\n",
"(0, 1)\n"
]
}
],
"source": [
"for v in g.vertices():\n",
"    print(v)\n",
"    \n",
"\n",
"for e in g.edges():\n",
"    print(e)\n",
"    \n"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## Iterating over the neighbors of a vertex"
]
},
{
"cell_type": "code",
"execution_count": 24,
"metadata": {},
"outputs": [
{
"name": "stdout",
"output_type": "stream",
"text": [
"(0, 1)\n",
"1\n"
]
}
],
"source": [
"# ptyhon way\n",
"for v in g.vertices():\n",
"   for e in v.out_edges():\n",
"       print(e)\n",
"   for w in v.out_neighbors():\n",
"       print(w)\n",
"    \n"
]
},
{
"cell_type": "code",
"execution_count": 25,
"metadata": {},
"outputs": [
{
"name": "stdout",
"output_type": "stream",
"text": [
"[1 0 0 0 0 0]\n"
]
}
],
"source": [
"# numpy way\n",
"\n",
"'''\n",
"Following the numpy philosophy, graph_tool also provides an array-based \n",
"interface that avoids loops in Python. This is done with the:\n",
"\n",
"- get_vertices()\n",
"- get_edges()\n",
"- get_out_edges()\n",
"- get_in_edges()\n",
"- get_all_edges()\n",
"- get_out_neighbors()\n",
"- get_in_neighbors()\n",
"- get_all_neighbors()\n",
"- get_out_degrees()\n",
"- get_in_degrees()\n",
"- get_total_degrees() methods\n",
"\n",
"All these function return numpy.ndarray instances instead of iterators.\n",
"'''\n",
"\n",
"print(g.get_out_degrees(g.get_vertices()))"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"# I/O"
]
},
{
"cell_type": "code",
"execution_count": 26,
"metadata": {},
"outputs": [],
"source": [
"# create a graph\n",
"g = Graph()\n",
"\n",
"# write data to a compressed, xml\n",
"g.save(\"my_graph.xml.gz\")\n",
"\n",
"# load data back\n",
"g2 = load_graph(\"my_graph.xml.gz\")"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"# Drawing a network"
]
},
{
"cell_type": "code",
"execution_count": 11,
"metadata": {},
"outputs": [
{
"data": {
"image/png": "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\n",
"text/plain": [
"<IPython.core.display.Image object>"
]
},
"metadata": {},
"output_type": "display_data"
},
{
"data": {
"text/plain": [
"<VertexPropertyMap object with value type 'vector<double>', for Graph 0x7fa2fcccc860, at 0x7fa2c5366908>"
]
},
"execution_count": 11,
"metadata": {},
"output_type": "execute_result"
}
],
"source": [
"# gt has a builtin function\n",
"graph_draw(g,\n",
"           vertex_text=g.vertex_index,\n",
"           vertex_font_size=18,\n",
"           output_size=(200, 200),\n",
"           #output=\"two-nodes.png\")\n",
"          )"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"# Fully-developed example\n",
"\n",
"The task consists of building a Price network (the one that existed before Barabasi). It is a directed network, with preferential attachment. "
]
},
{
"cell_type": "code",
"execution_count": 29,
"metadata": {},
"outputs": [],
"source": [
"# load libraries\n",
"from __future__ import division, absolute_import, print_function\n",
"import sys\n",
"if sys.version_info < (3,):\n",
"    range = xrange\n",
"import os\n",
"from pylab import *         # for plotting\n",
"from numpy.random import *  # for random sampling"
]
},
{
"cell_type": "code",
"execution_count": 30,
"metadata": {},
"outputs": [],
"source": [
"# fixing a seed that ensures reproducibility\n",
"seed(42)"
]
},
{
"cell_type": "code",
"execution_count": 31,
"metadata": {},
"outputs": [],
"source": [
"# empty graph\n",
"g = Graph()"
]
},
{
"cell_type": "code",
"execution_count": 32,
"metadata": {},
"outputs": [],
"source": [
"# create two containers in which we store vertex- and edge-level property\n",
"v_age = g.new_vertex_property(\"int\")\n",
"e_age = g.new_edge_property(\"int\")"
]
},
{
"cell_type": "code",
"execution_count": 33,
"metadata": {},
"outputs": [
{
"name": "stdout",
"output_type": "stream",
"text": [
"vertex: 36063 in-degree: 0 out-degree: 1 age: 36063\n",
"vertex: 9075 in-degree: 4 out-degree: 1 age: 9075\n",
"vertex: 5967 in-degree: 3 out-degree: 1 age: 5967\n",
"vertex: 1113 in-degree: 7 out-degree: 1 age: 1113\n",
"vertex: 25 in-degree: 84 out-degree: 1 age: 25\n",
"vertex: 10 in-degree: 541 out-degree: 1 age: 10\n",
"vertex: 5 in-degree: 140 out-degree: 1 age: 5\n",
"vertex: 2 in-degree: 459 out-degree: 1 age: 2\n",
"vertex: 1 in-degree: 520 out-degree: 1 age: 1\n",
"vertex: 0 in-degree: 210 out-degree: 0 age: 0\n",
"Nowhere else to go... We found the main hub!\n"
]
}
],
"source": [
"# network simulation\n",
"N = 100000\n",
"\n",
"# We have to start with one vertex\n",
"v = g.add_vertex()\n",
"v_age[v] = 0\n",
"\n",
"# we will keep a list of the vertices. The number of times a vertex is in this\n",
"# list will give the probability of it being selected.\n",
"vlist = [v]\n",
"\n",
"# let's now add the new edges and vertices\n",
"for i in range(1, N):\n",
"    # create our new vertex\n",
"    v = g.add_vertex()\n",
"    v_age[v] = i\n",
"\n",
"    # we need to sample a new vertex to be the target, based on its in-degree +\n",
"    # 1. For that, we simply randomly sample it from vlist.\n",
"    i = randint(0, len(vlist))\n",
"    target = vlist[i]\n",
"\n",
"    # add edge\n",
"    e = g.add_edge(v, target)\n",
"    e_age[e] = i\n",
"\n",
"    # put v and target in the list\n",
"    vlist.append(target)\n",
"    vlist.append(v)\n",
"\n",
"# now we have a graph!\n",
"\n",
"# let's do a random walk on the graph and print the age of the vertices we find,\n",
"# just for fun.\n",
"\n",
"v = g.vertex(randint(0, g.num_vertices()))\n",
"while True:\n",
"    print(\"vertex:\", int(v), \"in-degree:\", v.in_degree(), \"out-degree:\",\n",
"          v.out_degree(), \"age:\", v_age[v])\n",
"\n",
"    if v.out_degree() == 0:\n",
"        print(\"Nowhere else to go... We found the main hub!\")\n",
"        break\n",
"\n",
"    n_list = []\n",
"    for w in v.out_neighbors():\n",
"        n_list.append(w)\n",
"    v = n_list[randint(0, len(n_list))]\n",
"\n",
"# let's save our graph for posterity. We want to save the age properties as\n",
"# well... To do this, they must become \"internal\" properties:\n",
"\n",
"g.vertex_properties[\"age\"] = v_age\n",
"g.edge_properties[\"age\"] = e_age\n",
"\n",
"# now we can save it\n",
"g.save(\"price.xml.gz\")"
]
},
{
"cell_type": "code",
"execution_count": 37,
"metadata": {},
"outputs": [
{
"data": {
"image/png": "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\n",
"text/plain": [
"<Figure size 432x288 with 1 Axes>"
]
},
"metadata": {
"needs_background": "light"
},
"output_type": "display_data"
}
],
"source": [
"# get node in-degree\n",
"in_hist = vertex_hist(g, \"in\")\n",
"\n",
"# data series\n",
"# --+ point estimates\n",
"y = in_hist[0]\n",
"# --+ confidence interval\n",
"err = sqrt(in_hist[0])\n",
"err[err >= y] = y[err >= y] - 1e-2\n",
"\n",
"# create figure\n",
"figure(figsize=(6,4))\n",
"\n",
"# plot data with Matplotlib errorbar\n",
"errorbar(in_hist[1][:-1], in_hist[0],\n",
"         fmt=\"o\", alpha=0.5,\n",
"         yerr=err,\n",
"         label=\"in\")\n",
"\n",
"# axes\n",
"gca().set_yscale(\"log\")\n",
"gca().set_xscale(\"log\")\n",
"gca().set_ylim(1e-1, 1e5)\n",
"gca().set_xlim(0.8, 1e3)\n",
"\n",
"# \n",
"subplots_adjust(left=0.2, bottom=0.2)\n",
"\n",
"# labels\n",
"xlabel(\"$k_{in}$\")\n",
"ylabel(\"$Prob(k_{in})$\")\n",
"\n",
"# save figure\n",
"tight_layout()\n",
"savefig(\"price-deg-dist.pdf\")\n",
"savefig(\"price-deg-dist.svg\")"
]
},
{
"cell_type": "code",
"execution_count": 36,
"metadata": {},
"outputs": [
{
"data": {
"text/plain": [
"<VertexPropertyMap object with value type 'vector<double>', for Graph 0x7fa2ba614cc0, at 0x7fa2ba63e048>"
]
},
"execution_count": 36,
"metadata": {},
"output_type": "execute_result"
}
],
"source": [
"# drawing the simulated Price network\n",
"\n",
"# load data\n",
"g = load_graph(\"price.xml.gz\")\n",
"\n",
"# recall the age of vertices\n",
"age = g.vertex_properties[\"age\"]\n",
"\n",
"# create node-level positions\n",
"pos = sfdp_layout(g)\n",
"\n",
"# draw the network\n",
"graph_draw(g,\n",
"           pos,\n",
"           output_size=(1000, 1000),\n",
"           vertex_color=[1,1,1,0],\n",
"           vertex_fill_color=age,\n",
"           vertex_size=1,\n",
"           edge_pen_width=1.2,\n",
"           vcmap=matplotlib.cm.gist_heat_r,\n",
"           output=\"price.png\")"
]
}
],
"metadata": {
"kernelspec": {
"display_name": "Python 3",
"language": "python",
"name": "python3"
},
"language_info": {
"codemirror_mode": {
"name": "ipython",
"version": 3
},
"file_extension": ".py",
"mimetype": "text/x-python",
"name": "python",
"nbconvert_exporter": "python",
"pygments_lexer": "ipython3",
"version": "3.7.3"
}
},
"nbformat": 4,
"nbformat_minor": 2
}
