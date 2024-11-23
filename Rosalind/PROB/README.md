# ROSALIND | Introduction to Random Strings

https://rosalind.info/problems/prob/

Problem
-------

[![](https://rosalind.info/media/problems/prob/common_log.png)](https://rosalind.info/media/problems/prob/common_log.png)

**Figure 1**. The graph of the common logarithm function of x. For a given x-value, the corresponding y-value is the exponent to which we must raise 10 to obtain x. Note that x-values between 0 and 1 get mapped to y-values between -infinity and 0.

An [array](https://rosalind.info/glossary/array/) is a structure containing an ordered collection of objects (numbers, strings, other arrays, etc.). We let $A[k]$ denote the $k$\-th value in array $A$. You may like to think of an array as simply a [matrix](https://rosalind.info/glossary/matrix/) having only one row.

A [random string](https://rosalind.info/glossary/random-string/) is constructed so that the probability of choosing each subsequent symbol is based on a fixed underlying symbol frequency.

[GC-content](https://rosalind.info/glossary/gc-content/ "
The percentage of cytosine and guanine bases in a strand of nucleic acid.") offers us natural symbol frequencies for constructing random [DNA strings](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}."). If the GC-content is $x$, then we set the symbol frequencies of C and G equal to $\frac{x}{2}$ and the symbol frequencies of A and T equal to $\frac{1-x}{2}$. For example, if the GC-content is 40%, then as we construct the string, the next symbol is 'G'/'C' with probability 0.2, and the next symbol is 'A'/'T' with probability 0.3.

In practice, many probabilities wind up being very small. In order to work with small probabilities, we may plug them into a function that "blows them up" for the sake of comparison. Specifically, the [common logarithm](https://rosalind.info/glossary/common-logarithm/ "New term: 
The common logarithm of x is the exponent to which we must raise 10 to obtain x.") of $x$ (defined for $x > 0$ and denoted $\log\_{10}(x)$) is the exponent to which we must raise 10 to obtain $x$.

See [Figure 1](https://rosalind.info/media/problems/prob/common_log.png "Click to view") for a graph of the common logarithm function $y = \log\_{10}(x)$. In this graph, we can see that the logarithm of $x$\-values between 0 and 1 always winds up mapping to $y$\-values between $-\infty$ and 0: $x$\-values near 0 have logarithms close to $-\infty$, and $x$\-values close to 1 have logarithms close to $0$. Thus, we will select the common logarithm as our function to "blow up" small probability values for comparison.

Given: A [DNA string](https://rosalind.info/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") $s$ of length at most 100 [bp](https://rosalind.info/glossary/base-pair/ "
The combination of two bonded complementary bases.") and an array $A$ containing at most 20 numbers between 0 and 1.

Return: An array $B$ having the same length as $A$ in which $B[k]$ represents the common logarithm of the probability that a random string constructed with the GC-content found in $A[k]$ will match $s$ exactly.

Sample Dataset
--------------

```
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783

```


Sample Output
-------------

```
-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009

```


> Hint
> ----
> 
> One property of the logarithm function is that for any positive numbers $x$ and $y$, $\log\_{10}(x \cdot y) = \log\_{10}(x) + \log\_{10}(y)$.