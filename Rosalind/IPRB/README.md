# ROSALIND | Mendel's First Law

https://rosalind.info/problems/iprb/

Problem
-------

[![](https://rosalind.info/media/problems/iprb/balls_tree.thumb.png)](https://rosalind.info/media/problems/iprb/balls_tree.png)

**Figure 2**. The probability of any outcome (leaf) in a probability tree diagram is given by the product of probabilities from the start of the tree to the outcome. For example, the probability that X is blue and Y is blue is equal to (2/5)(1/4), or 1/10.

[Probability](https://rosalind.info/glossary/probability/ "New term: 
The mathematical study of the chance of occurrence of random events, or the chance with which
a specific event will occur.") is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a [random variable](https://rosalind.info/glossary/random-variable/ "New term: 
A variable that can take different values based on a randomized process."), which is simply a variable that can take a number of different distinct [outcomes](https://rosalind.info/glossary/outcome/ "New term: 
A possible value taken by a random variable.") depending on the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let $X$ represent the random variable corresponding to the color of a drawn ball, then the [probability](https://rosalind.info/glossary/probability/ "New term: 
The mathematical study of the chance of occurrence of random events, or the chance with which
a specific event will occur.") of each of the two outcomes is given by $\mathrm{Pr}(X = \textrm{red}) = \frac{3}{5}$ and $\mathrm{Pr}(X = \textrm{blue}) = \frac{2}{5}$.

Random variables can be combined to yield new random variables. Returning to the ball example, let $Y$ model the color of a second ball drawn from the bag (without replacing the first ball). The probability of $Y$ being red depends on whether the first ball was red or blue. To represent all outcomes of $X$ and $Y$, we therefore use a [probability tree diagram](https://rosalind.info/glossary/probability-tree-diagram/ "New term: 
A branching diagram representing all outcomes of multiple random variables."). This branching diagram represents all possible individual probabilities for $X$ and $Y$, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see [Figure 2](https://rosalind.info/media/problems/iprb/balls_tree.png "Click to view") for an illustrative example.

An [event](https://rosalind.info/glossary/probabilistic-event/ "New term: 
A collection of outcomes of a random variable.") is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let $A$ be the event "$Y$ is blue." $\mathrm{Pr}(A)$ is equal to the sum of the probabilities of two different outcomes: $\mathrm{Pr}(X = \textrm{blue and } Y = \textrm{blue}) + \mathrm{Pr}(X = \textrm{red and } Y = \textrm{blue})$, or $\frac{3}{10} + \frac{1}{10} = \frac{2}{5}$ (see Figure 2 above).

Given: Three positive integers $k$, $m$, and $n$, representing a population containing $k+m+n$ organisms: $k$ individuals are homozygous dominant for a factor, $m$ are heterozygous, and $n$ are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset
--------------
```
2 2 2
```
Sample Output
-------------
```
0.78333
```
