# ROSALIND | Matching Random Motifs

https://rosalind.info/problems/rstr/

Problem
-------

Our aim in this problem is to determine the [probability](https://rosalind.info/glossary/probability/ "
The mathematical study of the chance of occurrence of random events, or the chance with which
a specific event will occur.") with which a given motif (a known promoter, say) occurs in a randomly constructed genome. Unfortunately, finding this probability is tricky; instead of forming a long genome, we will form a large collection of smaller [random strings](https://rosalind.info/glossary/random-string/ "A string in which each symbol has a constant probability of occurring at any position.") having the same length as the motif; these smaller strings represent the genome's [substrings](https://rosalind.info/glossary/substring/ "
A substring of a given string is a contiguous string of symbols found in the string."), which we can then test against our motif.

Given a [probabilistic event](https://rosalind.info/glossary/probabilistic-event/ "
A collection of outcomes of a random variable.") $A$, the [complement](https://rosalind.info/glossary/complementary-event/ "New term: 
The opposite collection of outcomes of a given event.") of $A$ is the collection $A^{\textrm{c}}$ of [outcomes](https://rosalind.info/glossary/outcome/ "
A possible value taken by a random variable.") not belonging to $A$. Because $A^{\textrm{c}}$ takes place precisely when $A$ does not, we may also call $A^{\textrm{c}}$ "not $A$."

For a simple example, if $A$ is the event that a rolled die is 2 or 4, then $\mathrm{Pr}(A) = \frac{1}{3}$. $A^{\textrm{c}}$ is the event that the die is 1, 3, 5, or 6, and $\mathrm{Pr}(A^{\textrm{c}}) = \frac{2}{3}$. In general, for any event we will have the identity that $\mathrm{Pr(A)} + \mathrm{Pr}(A^{\textrm{c}}) = 1$.

Given: A positive integer $N \leq 100000$, a number $x$ between 0 and 1, and a DNA string $s$ of length at most 10 bp.

Return: The probability that if $N$ random DNA strings having the same length as $s$ are constructed with [GC-content](https://rosalind.info/glossary/gc-content/ "
The percentage of cytosine and guanine bases in a strand of nucleic acid.") $x$ (see [“Introduction to Random Strings”](https://rosalind.info/problems/prob/ "“Introduction to Random Strings”")), then at least one of the strings equals $s$. We allow for the same random string to be created more than once.

Sample Dataset
--------------
```
90000 0.6
ATAGCCGA
```

Sample Output
-------------
```
0.689
```