# ROSALIND | RNA Splicing

https://rosalind.info/problems/splc/

Problem
-------

After identifying the exons and introns of an [RNA string](https://rosalind.info/glossary/rna-string/ "
A string constructed from the alphabet {A, C, G, U}."), we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A [DNA string](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") $s$ (of length at most 1 [kbp](https://rosalind.info/glossary/kbp/ "
1 kbp = 1000 base pairs")) and a collection of [substrings](https://rosalind.info/glossary/substring/ "
A substring of a given string is a contiguous string of symbols found in the string.") of $s$ acting as introns. All strings are given in [FASTA format](https://rosalind.info/glossary/fasta-format/ "
A text format used for naming genetic strings in databases.").

Return: A [protein string](https://rosalind.info/glossary/protein-string/ "
A string composed of symbols taken from the English alphabet less B, J, O, U, X, and Z;
representing a peptide chain formed from amino acids.") resulting from transcribing and translating the exons of $s$. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
--------------
```
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
```

Sample Output
--------------
```
MVYIADKQHVASREAYGHMFKVCA
```
