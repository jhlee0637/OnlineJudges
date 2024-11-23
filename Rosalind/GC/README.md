# ROSALIND | Computing GC Content

https://rosalind.info/problems/gc/

Problem
-------

The GC-content of a [DNA string](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") is given by the percentage of [symbols](https://rosalind.info/glossary/symbol/ "
The constituent individual elements of a string, which may constitute numbers and letters.") in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the [reverse complement](https://rosalind.info/glossary/reverse-complement/ "
The DNA string formed by reversing and complementing each symbol.") of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called [FASTA format](https://rosalind.info/glossary/fasta-format/ "New term: 
A text format used for naming genetic strings in databases."). In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind\_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 [DNA strings](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") in FASTA format (of length at most 1 [kbp](https://rosalind.info/glossary/kbp/ "
1 kbp = 1000 base pairs") each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on [absolute error](https://rosalind.info/glossary/absolute-error/ "New term: A measure of how close a computed value is to a correct solution.") below.

Sample Dataset
--------------

```
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

```


Sample Output
-------------

> Note on Absolute Error
> ----------------------
> 
> We say that a number $x$ is within an absolute error of $y$ to a correct solution if $x$ is within $y$ of the correct solution. For example, if an exact solution is 6.157892, then for $x$ to be within an absolute error of 0.001, we must have that $|x - 6.157892| < 0.001$, or $6.156892 < x < 6.158892$.
> 
> Error bounding is a vital practical tool because of the inherent round-off error in representing decimals in a computer, where only a finite number of decimal places are allotted to any number. After being compounded over a number of operations, this round-off error can become evident. As a result, rather than testing whether two numbers are equal with $x = z$, you may wish to simply verify that $|x- z|$ is very small.
> 
> The mathematical field of [numerical analysis](https://rosalind.info/glossary/numerical-analysis/ "New term: 
> The mathematical study of computational approximation.") is devoted to rigorously studying the nature of computational approximation.