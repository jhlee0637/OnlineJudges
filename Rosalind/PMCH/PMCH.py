def getSeq(nameFile):
    seq=''
    with open(nameFile, 'r') as fr:
        reading=fr.readlines()
        for line in reading[1:]:
            line=line.strip()
            seq+=line
    return seq

def permutation(n):
    if n==1:
        m=1
    else:
        m=n*permutation(n-1)
    return m

if __name__ == "__main__":
    seq = getSeq('input.txt')
    cntA=seq.count('A')
    cntG=seq.count('G')
    answer=permutation(cntA)*permutation(cntG)
    print(answer)


'''
본문에 나온 complete graph를 구현하는 것으로 착각하였다.
실제로는 두 순열의 단순한 곱인데, 그 이유를 더 알아본다.

한 줄의 sequence가 주어지며, 이를 구성하는 뉴클레오타이드의 총 갯수는 짝수이고 A-U, G-C 짝을 남김없이 만들 수 있다.

G-C만을 생각해볼 때, 모든 G-C가 서로 중복없이 연결되는 방법을 생각해보자.
정답은 G의 수 만큼에 대한 수열인데, 이는 모든 C를 일렬로 나열해놓고 순서대로 G를 배정하는 방법을 생각하면 된다.

따라서 G-C짝을 만드는 모든 경우의 수는 G의 갯수만큼의 순열이며,
A-U짝은 A의 갯수만큼의 순열이다.

그리고 이 두 사건은 결합되므로 두 수를 곱한다.
'''