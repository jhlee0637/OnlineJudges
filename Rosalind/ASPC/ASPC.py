with open('input.txt', 'r') as fr:
    reading=fr.readline()
    
    # Given n and m
    n, m = map(int, reading.strip().split(" "))

# Calculate the total number of possible subsets
# Implement Factorial
def getFactorial(k):
    valFactorial=1
    for i in range(1, k+1):
        valFactorial*=i
    return valFactorial

#Implement Combination, following the option m<=k<=n
ans=0
for i in range(m, n+1):
    nFct=getFactorial(n)
    iFct=getFactorial(i)
    n_iFct=getFactorial(n-i)
    ans+=nFct//(iFct*n_iFct)

# answer = modulo 1M
print(ans%1000000)