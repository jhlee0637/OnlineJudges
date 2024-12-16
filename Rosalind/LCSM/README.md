# ROSALIND | Finding a Shared Motif

https://rosalind.info/problems/lcsm/

Problem
-------
A [common substring](https://rosalind.info/glossary/common-substring/ "New term: 
A substring contained in all strings from a collection.") of a collection of strings is a [substring](https://rosalind.info/glossary/substring/ "
A substring of a given string is a contiguous string of symbols found in the string.") of every member of the collection. We say that a common substring is a [longest common substring](https://rosalind.info/glossary/longest-common-substring/ "New term: 
A common substring of a collection of maximum length.") if there does not exist a longer common substring. For example, "CG" is a common substring of "A**CG**TACGT" and "AAC**CG**TATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "A**CGTA**CGT" and "AAC**CGTA**TA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of $k$ ($k \leq 100$) [DNA strings](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") of length at most 1 [kbp](https://rosalind.info/glossary/kbp/ "
1 kbp = 1000 base pairs") each in [FASTA format](https://rosalind.info/glossary/fasta-format/ "
A text format used for naming genetic strings in databases.").

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
--------------
```
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
```

Sample Output
-------------
```
AC
```