with open('input.txt', 'r') as fr:
    reading=fr.readline()
    
    # Given n
    n= int(reading.strip())

# Calculate the total number of possible subsets
# Implement Factorial
def getFactorial(k):
    valFactorial=1
    for i in range(1, k+1):
        valFactorial*=i
    return valFactorial

#Implement Combination
ans=0
for i in range(n+1):
    nFct=getFactorial(n)
    iFct=getFactorial(i)
    n_iFct=getFactorial(n-i)
    ans+=nFct//(iFct*n_iFct)

# answer = modulo 1M
print(ans%1000000)