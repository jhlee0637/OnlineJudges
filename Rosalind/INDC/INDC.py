import math

# Factorial
def factorial(n):
    val=1
    for i in range(1, n+1):
        val=val*i
    return val

# Combination
def combination(n, r):
    if r > n:
        return 0 
    val=factorial(n)//(factorial(n-r)*factorial(r))
    return val

# Binomial Distribution
def binomial(n, r, p):
    val=combination(n, r) * (p**r) * ((1-p)**(n-r))
    return val

with open('input.txt', 'r') as fr:
    reading=fr.readline()
    
    # Given n
    n = int(reading.strip())

answer=list()

# Sum the probability
for k in range(1, 2*n+1):
    prob=0

    # If k=1 -> Bin(10, 1, 0.5) + Bin(10, 2, 0.5) + ... + Bin(10, 10, 0.5)
    # If k=4 -> Bin(10, 4, 0.5) + Bin(10, 5, 0.5) + ... + Bin(10, 10, 0.5)
    # If k=10 -> Bin(10, 10, 0.5)
    for i in range(k, 2*n+1):
        biVal=binomial(2*n, i, 0.5)
        prob+=biVal
        val=round(math.log10(prob), 3)

    answer.append(val)

print(*answer)