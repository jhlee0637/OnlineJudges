# ROSALIND | Counting Subsets

https://rosalind.info/problems/sset/

Problem
-------
A [set](https://rosalind.info/glossary/set/ "New term: 
An unordered collection of objects called elements.") is the mathematical term for a loose collection of objects, called [elements](https://rosalind.info/glossary/element/ "New term: 
An object belonging to a set."). Examples of sets include $\{\textrm{the moon, the sun, Wilford Brimley}\}$ and $\mathbb{R}$, the set containing all real numbers. We even have the [empty set](https://rosalind.info/glossary/empty-set/ "New term: 
The set containing no elements, denoted by $\{\}$ or $\emptyset$."), represented by $\emptyset$ or $\{\}$, which contains no elements at all. Two sets are equal when they contain the same elements. In other words, in contrast to [permutations](https://rosalind.info/glossary/permutation/ "
A permutation of length n is an ordering of the first n positive integers."), the ordering of the elements of a set is unimportant (e.g., $\{\textrm{the moon, the sun, Wilford Brimley}\}$ is equivalent to $\{\textrm{Wilford Brimley, the moon, the sun}\}$). Sets are not allowed to contain duplicate elements, so that $\{\textrm{Wilford Brimley, the sun, the sun}\}$ is not a set. We have already used sets of 2 elements to represent [edges](https://rosalind.info/glossary/edge/ "
A segment or curve connecting two nodes in a graph.") from a [graph](https://rosalind.info/glossary/graph/ "
A network containing a collection of nodes, pairs of which are joined by edges.").

A set $A$ is a [subset](https://rosalind.info/glossary/subset/ "New term: A set whose elements are contained within another set.") of $B$ if every element of $A$ is also an element of $B$, and we write $A \subseteq B$. For example, $\{\textrm{the sun, the moon}\} \subseteq \{\textrm{the sun, the moon, Wilford Brimley}\}$, and $\emptyset$ is a subset of _every_ set (including itself!).

As illustrated in the biological introduction, we can use subsets to represent the collection of taxa possessing a character. However, the number of applications is endless; for example, an [event](https://rosalind.info/glossary/probabilistic-event/ "
A collection of outcomes of a random variable.") in [probability](https://rosalind.info/glossary/probability/ "
The mathematical study of the chance of occurrence of random events, or the chance with which
a specific event will occur.") can now be defined as a subset of the set containing all possible [outcomes](https://rosalind.info/glossary/outcome/ "
A possible value taken by a random variable.").

Our first question is to count the total number of possible subsets of a given set.

Given: A positive integer $n$ ($n \leq 1000$).

Return: The total number of subsets of $\{1, 2, \ldots, n\}$ [modulo](https://rosalind.info/glossary/modular-arithmetic/ "
The study of arithmetic on integer remainders.") 1,000,000.

Sample Dataset
--------------
```
3
```

Sample Output
-------------
```
8
```