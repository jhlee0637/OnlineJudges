# ROSALIND | Mortal Fibonacci Rabbits
https://rosalind.info/problems/fibd/recent/

### Problem
[![](https://rosalind.info/media/problems/fibd/mortal_rabbit_tree.thumb.png)](https://rosalind.info/media/problems/fibd/mortal_rabbit_tree.png)

**Figure 4**. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.

Recall the definition of the [Fibonacci numbers](https://rosalind.info/glossary/fibonacci-sequence/ "
A sequence of numbers formed by adding the two previous members of the sequence.") from [“Rabbits and Recurrence Relations”](https://rosalind.info/problems/fib/ "“Rabbits and Recurrence Relations”"), which followed the [recurrence relation](https://rosalind.info/glossary/recurrence-relation/ "
An equation defining the terms of a sequence with respect to previous terms.") $F_n = F_{n-1} + F_{n-2}$ and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a [dynamic programming](https://rosalind.info/glossary/dynamic-programming/ "
The algorithmic notion of building up a solution to a problem by solving it on progressively larger cases.") solution in the case that all rabbits die out after a fixed number of months. See [Figure 4](https://rosalind.info/media/problems/fibd/mortal_rabbit_tree.png "Click to view") for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

&emsp;Given: Positive integers $n \leq 100$ and $m \leq 20$.

&emsp;Return: The total number of pairs of rabbits that will remain after the $n$\-th month if all rabbits live for $m$ months.

### Sample Dataset
```
6 3
```
### Sample Output
```
4
```