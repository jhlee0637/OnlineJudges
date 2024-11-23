# ROSALIND | Locating Restriction Sites

https://rosalind.info/problems/revp/

Problem
-------

<img src="https://rosalind.info/media/problems/revp/palindrome.png" style='background-color: white'>

**Figure 2**. Palindromic recognition site

A [DNA string](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") is a [reverse palindrome](https://rosalind.info/glossary/reverse-palindrome/ "New term: 
A DNA string that is equal to its reverse complement.") if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See [Figure 2](https://rosalind.info/media/problems/revp/palindrome.png "Click to view").

Given: A [DNA string](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") of length at most 1 [kbp](https://rosalind.info/glossary/kbp/ "
1 kbp = 1000 base pairs") in [FASTA format](https://rosalind.info/glossary/fasta-format/ "
A text format used for naming genetic strings in databases.").

Return: The [position](https://rosalind.info/glossary/position/ "
The position of a symbol in a string is the total number of symbols found to
its left, including itself.") and [length](https://rosalind.info/glossary/string-length/ "
The number of symbols in a string.") of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
--------------

```
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

```


Sample Output
-------------
```
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4

```