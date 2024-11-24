# ROSALIND | Introduction to Alternative Splicing

https://rosalind.info/problems/aspc

Problem
-------
In [“Counting Subsets”](https://rosalind.info/problems/sset/ "“Counting Subsets”"), we saw that the total number of [subsets](https://rosalind.info/glossary/subset/ "A set whose elements are contained within another set.") of a [set](https://rosalind.info/glossary/set/ "
An unordered collection of objects called elements.") $S$ containing $n$ elements is equal to $2^n$.

However, if we intend to count the total number of [subsets](https://rosalind.info/glossary/subset/ "A set whose elements are contained within another set.") of $S$ having a fixed size $k$, then we use the [combination](https://rosalind.info/glossary/combination/ "New term: 
A statistic counting the total number of subsets of a fixed size taken from a set.") statistic $C(n, k)$, also written $\binom{n}{k}$.

Given: Positive integers $n$ and $m$ with $0 \leq m \leq n \leq 2000$.

Return: The sum of combinations $C(n, k)$ for all $k$ satisfying $m \leq k \leq n$, [modulo](https://rosalind.info/glossary/modular-arithmetic/ "
The study of arithmetic on integer remainders.") 1,000,000. In shorthand, $\sum_{k=m}^{n}{\binom{n}{k}}$.

Sample Dataset
--------------
```
6 3
```

Sample Output
-------------
```
8
```