# ROSALIND | Overlap Graphs

https://rosalind.info/problems/grph/

Problem
-------
A graph whose nodes have all been labeled can be represented by an [adjacency list](https://rosalind.info/glossary/adjacency-list/ "New term: 
A list containing the edges of a graph."), in which each row of the list contains the two node labels corresponding to a unique edge.

A [directed graph](https://rosalind.info/glossary/directed-graph/ "New term: 
A graph whose edges are oriented as arrows.") (or digraph) is a graph containing [directed edges](https://rosalind.info/glossary/directed-edge/ "New term: 
The oriented edge of a directed graph."), each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its [tail](https://rosalind.info/glossary/tail/ "New term: 
The starting node of a directed edge.") and [head](https://rosalind.info/glossary/head/ "New term: 
The ending node of a directed edge."), respectively. The directed edge with tail $v$ and head $w$ is represented by $(v, w)$ (but _not_ by $(w, v)$). A [directed loop](https://rosalind.info/glossary/directed-loop/ "New term: 
A directed edge $(v, v)$.") is a directed edge of the form $(v, v)$.

For a collection of strings and a positive integer $k$, the [overlap graph](https://rosalind.info/glossary/overlap-graph/ "New term: 
A directed graph representing overlap relationships in a collection of strings.") for the strings is a directed graph $O_k$ in which each string is represented by a node, and string $s$ is connected to string $t$ with a directed edge when there is a length $k$ [suffix](https://rosalind.info/glossary/suffix/ "
A substring of a given string that includes its final symbol.") of $s$ that matches a length $k$ [prefix](https://rosalind.info/glossary/prefix/ "
A substring of a given string that includes its first symbol.") of $t$, as long as $s \neq t$; we demand $s\neq t$ to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of [DNA strings](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") in [FASTA format](https://rosalind.info/glossary/fasta-format/ "
A text format used for naming genetic strings in databases.") having total length at most 10 [kbp](https://rosalind.info/glossary/kbp/ "
1 kbp = 1000 base pairs").

Return: The adjacency list corresponding to $O_3$. You may return edges in any order.

Sample Dataset
--------------

```
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

```


Sample Output
-------------

```
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323

```

> Note on Visualizing Graphs
> --------------------------
> 
> If you are looking for a way to actually visualize graphs as you are working through the Rosalind site, then you may like to consider [Graphviz](https://rosalind.info/glossary/graphviz/ "New term: 
> A free cross-platform program for rendering graphs.") (link [here](http://www.graphviz.org/)), a cross-platform application for rendering graphs.