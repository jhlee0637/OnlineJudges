# Consensus and Profile

https://rosalind.info/problems/cons/

### Problem
A [matrix](https://rosalind.info/glossary/matrix/ "New term: 
A rectangular table of values arranged in rows and columns.") is a rectangular table of values divided into rows and columns. An $m \text{ x } n$ matrix has $m$ rows and $n$ columns. Given a matrix $A$, we write $A_{i, j}$ to indicate the value found at the intersection of row $i$ and column ***j***.

Say that we have a collection of [DNA strings](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}."), all having the same length $n$. Their [profile matrix](https://rosalind.info/glossary/profile-matrix/ "New term: 
A matrix encoding the number of times that each symbol of an alphabet occurs in each
position from a collection of strings.") is a $4 \text{ x } n$ [matrix](https://rosalind.info/glossary/matrix/ "
A rectangular table of values arranged in rows and columns.") $P$ in which $P_{1,j}$ represents the number of times that 'A' occurs in the ***j***th [position](https://rosalind.info/glossary/position/ "
The position of a symbol in a string is the total number of symbols found to
its left, including itself.") of one of the strings, $P_{2,j}$ represents the number of times that C occurs in the ***j***th position, and so on (see below).

A [consensus string](https://rosalind.info/glossary/consensus-string/ "New term: 
A string formed from a collection of equal-length strings by taking the most common symbol at each position.") $c$ is a string of length $n$ formed from our collection by taking the most common symbol at each position; the ***j***th symbol of $c$ therefore corresponds to the symbol having the maximum value in the ***j***th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

&emsp; Given: A collection of at most 10 [DNA strings](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") of equal length (at most 1 [kbp](https://rosalind.info/glossary/kbp/ "
1 kbp = 1000 base pairs")) in [FASTA format](https://rosalind.info/glossary/fasta-format/ "
A text format used for naming genetic strings in databases.").

&emsp;Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

### Sample Dataset
```
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
```

### Sample Output
```
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
```
