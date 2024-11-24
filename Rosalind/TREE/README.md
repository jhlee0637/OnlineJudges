# ROSALIND | Completing a Tree

https://rosalind.info/problems/tree

Problem
-------

[![](https://rosalind.info/media/problems/tree/tree_graph.png)](https://rosalind.info/media/problems/tree/tree_graph.png)

**Figure 2**. A labeled tree with 6 vertices and 5 edges.

An undirected [graph](https://rosalind.info/glossary/graph/ "
A network containing a collection of nodes, pairs of which are joined by edges.") is [connected](https://rosalind.info/glossary/connected-graph/ "New term: 
A graph in which there exists a path between any two nodes.") if there is a [path](https://rosalind.info/glossary/path/ "
A collection of nodes and edges in which each node is connected to the next via an edge.") connecting any two [nodes](https://rosalind.info/glossary/node/ "
A point forming the hubs of the network represented by a graph."). A [tree](https://rosalind.info/glossary/tree/ "New term: 
A connected graph containing no cycles.") is a connected (undirected) graph containing no [cycles](https://rosalind.info/glossary/cycle/ "
A path in a graph that begins and ends in the same node."); this definition forces the tree to have a branching structure organized around a central core of nodes, just like its living counterpart. See [Figure 2](https://rosalind.info/media/problems/tree/tree_graph.png "Click to view").

We have already grown familiar with trees in [“Mendel's First Law”](https://rosalind.info/problems/iprb/ "“Mendel's First Law”"), where we introduced the [probability tree diagram](https://rosalind.info/glossary/probability-tree-diagram/ "
A branching diagram representing all outcomes of multiple random variables.") to visualize the [outcomes](https://rosalind.info/glossary/outcome/ "
A possible value taken by a random variable.") of a [random variable](https://rosalind.info/glossary/random-variable/ "
A variable that can take different values based on a randomized process.").

In the creation of a phylogeny, taxa are encoded by the tree's [leaves](https://rosalind.info/glossary/leaf/ "New term: 
A node in a tree having degree equal to 1."), or nodes having [degree](https://rosalind.info/glossary/degree/ "
The number of edges incident to a node.") 1. A node of a tree having degree larger than 1 is called an [internal node](https://rosalind.info/glossary/internal-node/ "New term: 
A node of a tree having degree at least 2.").

Given: A positive integer $n$ ($n \leq 1000$) and an [adjacency list](https://rosalind.info/glossary/adjacency-list/ "
A list containing the edges of a graph.") corresponding to a graph on $n$ nodes that contains no cycles.

Return: The minimum number of [edges](https://rosalind.info/glossary/edge/ "
A segment or curve connecting two nodes in a graph.") that can be added to the graph to produce a tree.

Sample Dataset
--------------
```
10
1 2
2 8
4 10
5 9
6 10
7 9
```

Sample Output
-------------
```
3
```