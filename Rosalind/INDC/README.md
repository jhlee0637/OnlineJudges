# ROSALIND | Independent Segregation of Chromosomes

https://rosalind.info/problems/indc/

Problem
----------------------
Consider a collection of coin flips. One of the most natural questions we can ask is if we flip a coin 92 times, what is the [probability](https://rosalind.info/glossary/probability/ "
The mathematical study of the chance of occurrence of random events, or the chance with which
a specific event will occur.") of obtaining 51 "heads", vs. 27 "heads", vs. [92 "heads"](http://en.wikipedia.org/wiki/Rosencrantz_and_Guildenstern_Are_Dead)?

Each coin flip can be modeled by a [uniform random variable](https://rosalind.info/glossary/uniform-random-variable/ "
A random variable in which equally spaced outcomes have the same probability.") in which each of the two [outcomes](https://rosalind.info/glossary/outcome/ "
A possible value taken by a random variable.") ("heads" and "tails") has probability equal to 1/2. We may assume that these random variables are [independent](https://rosalind.info/glossary/independent-random-variables/ "
Two random variables whose outcomes occur with no dependence on the other random variable.") (see [“Independent Alleles”](https://rosalind.info/problems/lia/ "“Independent Alleles”")); in layman's terms, the outcomes of the two coin flips do not influence each other.

A [binomial random variable](https://rosalind.info/glossary/binomial-random-variable/ "New term: 
A random variable counting the total number of \"heads\" obtained from a fixed number of (possibly
weighted) coin flips.") $X$ takes a value of $k$ if $n$ consecutive "coin flips" result in $k$ total "heads" and $n-k$ total "tails." We write that $X \in \mathrm{Bin}(n, 1/2)$.

Given: A positive integer $n \leq 50$.

Return: An [array](https://rosalind.info/glossary/array/ "
A data structure that has a collection of ordered locations to which objects may be assigned.") $A$ of length $2n$ in which $A[k]$ represents the [common logarithm](https://rosalind.info/glossary/common-logarithm/ "
The common logarithm of x is the exponent to which we must raise 10 to obtain x.") of the probability that two diploid siblings share at least $k$ of their $2n$ chromosomes (we do not consider [recombination](https://rosalind.info/glossary/genetic-recombination/ "
The exchange of alleles between homologous chromosomes during meiosis.") for now).

Sample Dataset
---
```
5
```

Sample Output
---
```
0.000 -0.004 -0.024 -0.082 -0.206 -0.424 -0.765 -1.262 -1.969 -3.010
```