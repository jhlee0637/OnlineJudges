'''
https://rosalind.info/problems/fib/

Wascally Wabbits: In 1202, Leonardo of Pisa (commonly known as Fibonacci) considered a mathematical exercise regarding the reproduction of a population of rabbits.
                  He made the following simplifying assumptions about the population:
                    The population begins in the first month with a pair of newborn rabbits.
                    Rabbits reach reproductive age after one month.
                    In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
                    Exactly one month after two rabbits mate, they produce one male and one female rabbit.
                    Rabbits never die or stop reproducing.
                  Fibonacci's exercise was to calculate how many pairs of rabbits would remain in one year.
                  We can see that in the second month, the first pair of rabbits reach reproductive age and mate.
                  In the third month, another pair of rabbits is born, and we have two rabbit pairs; our first pair of rabbits mates again.
                  In the fourth month, another pair of rabbits is born to the original pair, while the second pair reach maturity and mate (with three total pairs).
                  The dynamics of the rabbit population are illustrated in Figure 1. After a year, the rabbit population boasts 144 pairs.
                  Although Fibonacci's assumption of the rabbits' immortality may seem a bit farfetched,
                  his model was not unrealistic for reproduction in a predator-free environment:
                  European rabbits were introduced to Australia in the mid 19th Century,
                  a place with no real indigenous predators for them. Within 50 years,
                  the rabbits had already eradicated many plant species across the continent,
                  leading to irreversible changes in the Australian ecosystem and turning much of its grasslands into eroded,
                  practically uninhabitable parts of the modern Outback (see Figure 2).
                  In this problem, we will use the simple idea of counting rabbits to introduce a new computational topic,
                  which involves building up large solutions from smaller ones.

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months,
        if we begin with 1 pair and in each generation,
        every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Sample Dataset: 5 3
Sample Output: 19
'''
def fib(n,k):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return fib(n-1,k)+fib(n-2,k)*k

if __name__=="__main__":
    n=5
    k=3
    #n=
    #k=
    print(fib(n-1,k))

    