# ROSALIND | Perfect Matchings and RNA Secondary Structures

https://rosalind.info/problems/pmch/

Problem
-------
>[![](https://rosalind.info/media/problems/pmch/matching.thumb.png)](https://rosalind.info/media/problems/pmch/matching.png)
>
>**Figure 2**. Three matchings (highlighted in red) shown in three different graphs.

>[![](https://rosalind.info/media/problems/pmch/perfect_matching.thumb.png)](https://rosalind.info/media/problems/pmch/perfect_matching.png)
>
>**Figure 3**. A graph containing 10 nodes; the five edges forming a perfect matching on these nodes are highlighted in red.

>[![](https://rosalind.info/media/problems/pmch/bonding_graph.thumb.png)](https://rosalind.info/media/problems/pmch/bonding_graph.png)
>
>**Figure 4**. The bonding graph for the RNA string s = UAGCGUGAUCAC.

>[![](https://rosalind.info/media/problems/pmch/bonding_crossing.thumb.png)](https://rosalind.info/media/problems/pmch/bonding_crossing.png)
>
>**Figure 5**. A perfect matching on the basepair edges is highlighted in red and represents a candidate secondary structure for the RNA strand.

A [matching](https://rosalind.info/glossary/matching/ "New term: 
A collection of edges in a graph, no two of which include the same node.") in a [graph](https://rosalind.info/glossary/graph/ "
A network containing a collection of nodes, pairs of which are joined by edges.") $\mathrm{G}$ is a collection of [edges](https://rosalind.info/glossary/edge/ "
A segment or curve connecting two nodes in a graph.") of $\mathrm{G}$ for which no node belongs to more than one edge in the collection. See [Figure 2](https://rosalind.info/media/problems/pmch/matching.png "Click to view") for examples of matchings. If $G$ contains an even number of nodes (say $2n$), then a matching on $G$ is [perfect](https://rosalind.info/glossary/perfect-matching/ "New term: 
A matching that includes every node in a graph.") if it contains $n$ edges, which is clearly the maximum possible. An example of a graph containing a perfect matching is shown in [Figure 3](https://rosalind.info/media/problems/pmch/perfect_matching.png "Click to view").

First, let $K_n$ denote the [complete graph](https://rosalind.info/glossary/complete-graph/ "New term: 
A graph in which every node is connected by an edge to every other node.") on $2n$ labeled nodes, in which every [node](https://rosalind.info/glossary/node/ "
A point forming the hubs of the network represented by a graph.") is connected to every other node with an edge, and let $p_n$ denote the total number of perfect matchings in $K_n$. For a given node $x$, there are $2n - 1$ ways to join $x$ to the other nodes in the graph, after which point we must form a perfect matching on the remaining $2n - 2$ nodes. This reasoning provides us with the [recurrence relation](https://rosalind.info/glossary/recurrence-relation/ "
An equation defining the terms of a sequence with respect to previous terms.") $p_n = (2n - 1)\cdot p_{n-1}$; using the fact that $p_1$ is 1, this recurrence relation implies the closed equation $p_n = (2n - 1)(2n - 3)(2n - 5)\cdots (3)(1)$.

Given an [RNA string](https://rosalind.info/glossary/rna-string/ "
A string constructed from the alphabet {A, C, G, U}.") $s = s_1 \ldots s_n$, a [bonding graph](https://rosalind.info/glossary/bonding-graph/ "New term: 
A graph used to model base pairing in RNA secondary structure.") for $s$ is formed as follows. First, assign each symbol of $s$ to a node, and arrange these nodes in order around a circle, connecting them with edges called [adjacency edges](https://rosalind.info/glossary/adjacency-edges/ "New term: 
Edges in the bonding graph of an RNA string connecting adjacent symbols in the string."). Second, form all possible edges {A, U} and {C, G}, called [basepair edges](https://rosalind.info/glossary/basepair-edges/ "New term: 
Edges in the bonding graph of an RNA string connecting potential base pairs."); we will represent basepair edges with dashed edges, as illustrated by the bonding graph in [Figure 4](https://rosalind.info/media/problems/pmch/bonding_graph.png "Click to view").

Note that a matching contained in the basepair edges will represent one possibility for base pairing interactions in $s$, as shown in [Figure 5](https://rosalind.info/media/problems/pmch/bonding_crossing.png "Click to view"). For such a matching to exist, $s$ must have the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Given: An RNA string $s$ of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of _perfect_ matchings of basepair edges in the bonding graph of $s$.

Sample Dataset
--------------
```
>Rosalind_23
AGCUAGUCAU
```

Sample Output
-------------
```
12
```