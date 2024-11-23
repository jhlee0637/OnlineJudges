# ROSALIND | Counting Point Mutations

https://rosalind.info/problems/hamm/

Problem
-------

[![](https://rosalind.info/media/problems/hamm/Hamming_distance.png)](https://rosalind.info/media/problems/hamm/Hamming_distance.png)

**Figure 2**. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.

Given two [strings](https://rosalind.info/glossary/string/ "
An ordered collection of symbols formed into a word.") $s$ and $t$ of equal length, the [Hamming distance](https://rosalind.info/glossary/hamming-distance/ "New term: 
The minimum number of symbol substitutions required to change one string into another of equal length.") between $s$ and $t$, denoted $d_{H}(s, t)$, is the number of corresponding symbols that differ in $s$ and $t$. See [Figure 2](https://rosalind.info/media/problems/hamm/Hamming_distance.png "Click to view").

Given: Two [DNA strings](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") $s$ and $t$ of equal length (not exceeding 1 [kbp](https://rosalind.info/glossary/kbp/ "
1 kbp = 1000 base pairs")).

Return: The Hamming distance $d_{H}(s, t)$.

Sample Dataset
--------------
```
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

```

Sample Output
-------------
```
7
```