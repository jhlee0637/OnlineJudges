# ROSALIND | Calculating Protein Mass

https://rosalind.info/problems/prtm/recent/

Problem
-------

In a [weighted alphabet](https://rosalind.info/glossary/weighted-alphabet/ "New term: 
An alphabet in which every symbol is assigned a (positive) real number."), every symbol is assigned a positive real number called a [weight](https://rosalind.info/glossary/symbol-weight/ "New term: 
The weight of a symbol is a positive real number assigned to it."). A string formed from a weighted alphabet is called a [weighted string](https://rosalind.info/glossary/weighted-string/ "New term: 
A string whose symbols are equipped with underlying weights."), and its [weight](https://rosalind.info/glossary/string-weight/ "New term: 
The sum of the weights of all the string's symbols.") is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

Given: A protein string $P$ of length at most 1000 [aa](https://rosalind.info/glossary/amino-acid/ "
The monomer unit for proteins; the same 20 amino acids commonly occur in most species.").

Return: The total weight of $P$. Consult the [monoisotopic mass table](https://rosalind.info/glossary/monoisotopic-mass-table/ "New term: 
A table of amino acid residues based on monoisotopic masses.").

Sample Dataset
--------------
```
SKADYEK
```
Sample Output
-------------
```
821.392
```