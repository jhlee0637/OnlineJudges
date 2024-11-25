import numpy as np
import math
n=int(input())

Pr=0
p=0.5
A=[]
for k in range(2*n,0,-1):
    Pr+=math.factorial(2*n)/(math.factorial(k)*math.factorial(2*n-k))*np.power(p,k)*np.power(1-p,2*n-k)
    A.append(round(np.log10(Pr),3))

f=open(r"C:\Users\J\OneDrive\MyCoding\OnlineJudges\Rosalind\INDC\output.txt",'w')
for i in A[::-1]:
    print(i,end=' ',file=f)