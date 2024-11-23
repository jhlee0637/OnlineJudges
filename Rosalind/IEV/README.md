# ROSALIND | Calculating Expected Offspring

https://rosalind.info/problems/iev/

Problem
-------

For a [random variable](https://rosalind.info/glossary/random-variable/ "
A variable that can take different values based on a randomized process.") $X$ taking integer values between 1 and $n$, the [expected value](https://rosalind.info/glossary/expected-value/ "New term: 
The average case of a random variable over time.") of $X$ is $\mathrm{E}(X) = \sum\_{k=1}^{n}{k \times \mathrm{Pr}(X = k)}$. The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.

As a motivating example, let $X$ be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value confirms that $\mathrm{E}(X) = \sum\_{k=1}^{6} k \times \mathrm{Pr}(X = k) = 3.5$.

More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a [uniform random variable](https://rosalind.info/glossary/uniform-random-variable/ "New term: 
A random variable in which equally spaced outcomes have the same probability.") (in the die example, this "equal spacing" is equal to 1). We can generalize our die example to find that if $X$ is a uniform random variable with minimum possible value $a$ and maximum possible value $b$, then $\mathrm{E}(X) = \frac{a+b}{2}$. You may also wish to verify that for the dice example, if $Y$ is the random variable associated with the outcome of a second die roll, then $\mathrm{E}(X+Y) = 7$.

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each [genotype](https://rosalind.info/glossary/genotype/ "
An organism's precise genetic makeup.") pairing for a given [factor](https://rosalind.info/glossary/factor/ "
The Mendelian unit of heredity."). In order, the six given integers represent the number of couples having the following genotypes:

1.  AA-AA
2.  AA-Aa
3.  AA-aa
4.  Aa-Aa
5.  Aa-aa
6.  aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

Sample Dataset
--------------
```
1 0 0 1 0 1
```

Sample Output
-------------
```
3.5
```