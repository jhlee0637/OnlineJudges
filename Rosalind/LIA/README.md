# ROSALIND | Independent Alleles

https://rosalind.info/problems/lia/

Problem
-------
> [![](https://rosalind.info/media/problems/lia/two_dice.thumb.png)](https://rosalind.info/media/problems/lia/two_dice.png)
>
> **Figure 2**. The probability of each outcome for the sum of the values on two rolled dice (black and white), broken down depending on the number of pips showing on each die. You can verify that 18 of the 36 equally probable possibilities result in an odd sum.

Two [events](https://rosalind.info/glossary/probabilistic-event/ "
A collection of outcomes of a random variable.") $A$ and $B$ are [independent](https://rosalind.info/glossary/independent-events/ "New term: 
Events whose probabilities of occurring do not influence one another.") if $\mathrm{Pr}(A \textrm{ and } B)$ is equal to $\mathrm{Pr}(A) \times \mathrm{Pr}(B)$. In other words, the events do not influence each other, so that we may simply calculate each of the individual probabilities separately and then multiply.

More generally, [random variables](https://rosalind.info/glossary/random-variable/ "
A variable that can take different values based on a randomized process.") $X$ and $Y$ are [independent](https://rosalind.info/glossary/independent-random-variables/ "New term: 
Two random variables whose outcomes occur with no dependence on the other random variable.") if whenever $A$ and $B$ are respective events for $X$ and $Y$, $A$ and $B$ are independent (i.e., $\mathrm{Pr}(A \textrm{ and } B) = \mathrm{Pr}(A) \times \mathrm{Pr}(B)$).

As an example of how helpful independence can be for calculating probabilities, let $X$ and $Y$ represent the numbers showing on two six-sided dice. Intuitively, the number of pips showing on one die should not affect the number showing on the other die. If we want to find the probability that $X + Y$ is odd, then we don't need to draw a tree diagram and consider all possibilities. We simply first note that for $X+Y$ to be odd, either $X$ is even and $Y$ is odd or $X$ is odd and $Y$ is even. In terms of probability, $\mathrm{Pr}(X+Y \textrm{ is odd}) = \mathrm{Pr}(X \textrm{ is even and } Y \textrm{ is odd}) + \mathrm{Pr}(X \textrm{ is odd and } Y \textrm{ is even})$. Using independence, this becomes $\left[\mathrm{Pr}(X \textrm{ is even}) \times \mathrm{Pr}(Y \textrm{ is odd})\right] + \left[\mathrm{Pr}(X \textrm{ is odd}) \times \mathrm{Pr}(Y \textrm{ is even})\right]$, or $\left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 = \frac{1}{2}$. You can verify this result in [Figure 2](https://rosalind.info/media/problems/lia/two_dice.png "Click to view"), which shows all 36 outcomes for rolling two dice.

Given: Two positive integers $k$ ($k \leq 7$) and $N$ ($N \leq 2^k$). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least $N$ Aa Bb organisms will belong to the $k$\-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

Sample Dataset
--------------
```
2 1
```

Sample Output
-------------
```
0.684
```