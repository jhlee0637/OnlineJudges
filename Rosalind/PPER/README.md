# ROSALIND | Partial Permutations

https://rosalind.info/problems/pper

Problem
-------

A [partial permutation](https://rosalind.info/glossary/partial-permutation/ "New term: 
An ordering of some of the objects from a collection.") is an ordering of only $k$ objects taken from a collection containing $n$ objects (i.e., $k \leq n$). For example, one partial permutation of three of the first eight positive integers is given by $(5, 7, 2)$.

The statistic $P(n, k)$ counts the total number of partial permutations of $k$ objects that can be formed from a collection of $n$ objects. Note that $P(n, n)$ is just the number of permutations of $n$ objects, which we found to be equal to $n! = n (n-1) (n-2) \cdots (3) (2)$ in [“Enumerating Gene Orders”](https://rosalind.info/problems/perm/ "“Enumerating Gene Orders”").

Given: Positive integers $n$ and $k$ such that $100 \geq n > 0$ and $10 \geq k > 0$.

Return: The total number of partial permutations $P(n, k)$, [modulo](https://rosalind.info/glossary/modular-arithmetic/ "
The study of arithmetic on integer remainders.") 1,000,000.

Sample Dataset
--------------
```
21 7
```

Sample Output
-------------
```
51200
```