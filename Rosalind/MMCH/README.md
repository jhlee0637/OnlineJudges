# ROSALIND | Maximum Matchings and RNA Secondary Structures

https://rosalind.info/problems/mmch/

Problem
-------
The [graph theoretical](https://rosalind.info/glossary/graph-theory/ "
The abstract mathematical study of graphs, or networks.") analogue of the quandary stated in the introduction above is that if we have an [RNA string](https://rosalind.info/glossary/rna-string/ "
A string constructed from the alphabet {A, C, G, U}.") $s$ that does not have the same number of occurrences of 'C' as 'G' and the same number of occurrences of 'A' as 'U', then the [bonding graph](https://rosalind.info/glossary/bonding-graph/ "
A graph used to model base pairing in RNA secondary structure.") of $s$ cannot possibly possess a [perfect matching](https://rosalind.info/glossary/perfect-matching/ "
A matching that includes every node in a graph.") among its [basepair edges](https://rosalind.info/glossary/basepair-edges/ "
Edges in the bonding graph of an RNA string connecting potential base pairs."). For example, see [Figure 1](https://rosalind.info/media/problems/mmch/unbalanced_bonding_graph.png "Click to view"); in fact, most bonding graphs will not contain a perfect matching.

In light of this fact, we define a [maximum matching](https://rosalind.info/glossary/maximum-matching/ "New term: 
A matching in a graph that contains the maximum possible number of nodes.") in a graph as a [matching](https://rosalind.info/glossary/matching/ "
A collection of edges in a graph, no two of which include the same node.") containing as many [edges](https://rosalind.info/glossary/edge/ "
A segment or curve connecting two nodes in a graph.") as possible. See [Figure 2](https://rosalind.info/media/problems/mmch/maximum_matching.png "Click to view") for three maximum matchings in graphs.

A maximum matching of basepair edges will correspond to a way of forming as many base pairs as possible in an RNA string, as shown in [Figure 3](https://rosalind.info/media/problems/mmch/maximum_matching_bonding.png "Click to view").

Given: An RNA string $s$ of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of $s$.

Sample Dataset
--------------
```
>Rosalind_92
AUGCUUC
```
Sample Output
-------------
```
6
```