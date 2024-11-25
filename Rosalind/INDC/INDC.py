import math

with open('input.txt', 'r') as fr:
    reading=fr.readline()
    
    # Given n
    n = int(reading.strip())

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

for r in range(2*n):
    cuVal=0
    biVal=binomial(2*n, r, 0.5)
    cuVal+=biVal
    print(r, math.log10(cuVal))