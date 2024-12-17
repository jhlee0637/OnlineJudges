def getSeq(file_name):
    seq=''
    with open(file_name, 'r') as fr:
        reading=fr.readlines()
        for line in reading[1:]:
            line=line.strip()
            seq+=line
    return seq

def factorial(n):
    if n==1:
        m=1
    else:
        m=n*factorial(n-1)
    return m

def combination(n, r):
    nCr=factorial(n)//(factorial(r)*factorial(n-r)) #정수형으로 표현하기 위해 //를 사용
    return nCr

def getMaxMatch(cntN, cntM):
    #case0. zero
    if cntN==0 or cntM==0:
        maxMatch=0
    #case1. equal
    elif cntN==cntM:
        maxMatch=factorial(cntN)
    #case2. unequal
    else:
        maxCnt=max(cntN, cntM)
        minCnt=min(cntN, cntM)
        maxMatch=combination(maxCnt, minCnt) * factorial(minCnt) #이 부분은 순열과 같은 공식이 된다.
        #maxMatch=factorial(maxCnt)//factorial(maxCnt-minCnt)
    return maxMatch

if __name__=="__main__":
    file_name='input.txt'
    seq=getSeq(file_name)
    #get count of bases
    cntA=seq.count('A')
    cntU=seq.count('U')
    cntG=seq.count('G')
    cntC=seq.count('C')
    #get maximum matching value of A-U
    maxMatchAU = getMaxMatch(cntA, cntU)
    #get maximum matching value of G-C
    maxMatchGC = getMaxMatch(cntG, cntC)
    #times the maximum matches
    if maxMatchAU==0 or maxMatchGC==0:
        answer=max(maxMatchAU, maxMatchGC)
    else:
        answer=maxMatchAU * maxMatchGC
    print(answer)

'''
예를 들어 A가 10개, U가 12개가 있다고 하자.
이때 perfect match를 만들기 위해서는 먼저 U 12개 중 10개를 순서에 상관없이 뽑는 경우의 수(조합)을 알아야 한다.
그 다음 일렬로 나열된 U에 대해서 A를 각각 연결한다(팩토리얼)

이렇게 A-U, G-C를 모두 구한 다음, 이는 결합사건이므로 곱한다.
'''