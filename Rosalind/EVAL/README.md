# ROSALIND | Expected Number of Restriction Sites

https://rosalind.info/problems/eval/

Problem
-------

Say that you place a number of bets on your favorite sports teams. If their chances of winning are 0.3, 0.8, and 0.6, then you should expect on average to win 0.3 + 0.8 + 0.6 = 1.7 of your bets (of course, you can never win exactly 1.7!)

More generally, if we have a collection of [events](https://rosalind.info/glossary/probabilistic-event/ "
A collection of outcomes of a random variable.") $A\_1, A\_2, \ldots, A\_n$, then the [expected number](https://rosalind.info/glossary/expected-value/ "
The average case of a random variable over time.") of events occurring is $\mathrm{Pr}(A\_1) + \mathrm{Pr}(A\_2) + \cdots + \mathrm{Pr}(A\_n)$ (consult the note following the problem for a precise explanation of this fact). In this problem, we extend the idea of finding an expected number of events to finding the expected number of times that a given string occurs as a [substring](https://rosalind.info/glossary/substring/ "
A substring of a given string is a contiguous string of symbols found in the string.") of a [random string](https://rosalind.info/glossary/random-string/ "A string in which each symbol has a constant probability of occurring at any position.").

Given: A positive integer $n$ ($n \leq 1,000,000$), a DNA string $s$ of even length at most 10, and an [array](https://rosalind.info/glossary/array/ "
A data structure that has a collection of ordered locations to which objects may be assigned.") $A$ of length at most 20, containing numbers between 0 and 1.

Return: An array $B$ having the same length as $A$ in which $B[i]$ represents the expected number of times that $s$ will appear as a substring of a random DNA string $t$ of length $n$, where $t$ is formed with [GC-content](https://rosalind.info/glossary/gc-content/ "
The percentage of cytosine and guanine bases in a strand of nucleic acid.") $A[i]$ (see [“Introduction to Random Strings”](https://rosalind.info/problems/prob/ "“Introduction to Random Strings”")).

Sample Dataset
--------------
```
10
AG
0.25 0.5 0.75
```
Sample Output
-------------
```
0.422 0.563 0.422
```
