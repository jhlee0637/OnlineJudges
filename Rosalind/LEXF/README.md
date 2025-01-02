# ROSALIND | Enumerating k-mers Lexicographically

https://rosalind.info/problems/lexf/

Problem
-------

Assume that an [alphabet](https://rosalind.info/glossary/alphabet/ "
A collection of symbols from which strings are constructed.") $\mathscr{A}$ has a predetermined order; that is, we write the alphabet as a [permutation](https://rosalind.info/glossary/permutation/ "
A permutation of length n is an ordering of the first n positive integers.") $\mathscr{A} = (a\_1, a\_2, \ldots, a\_k)$, where $a\_1 < a\_2 < \cdots < a\_k$. For instance, the English alphabet is organized as $(\textrm{A}, \textrm{B}, \ldots, \textrm{Z})$.

Given two strings $s$ and $t$ having the same length $n$, we say that $s$ precedes $t$ in the [lexicographic order](https://rosalind.info/glossary/lexicographic-order/ "New term: 
A \"dictionary\" ordering of strings constructed from the same ordered alphabet.") (and write $s <\_{\textrm{Lex}} t$) if the first symbol $s[j]$ that doesn't match $t[j]$ satisfies $s\_j < t\_j$ in $\mathscr{A}$.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer $n$ ($n \leq 10$).

Return: All strings of length $n$ that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

Sample Dataset
--------------
```
A C G T
2
```
Sample Output
-------------

```
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT

```