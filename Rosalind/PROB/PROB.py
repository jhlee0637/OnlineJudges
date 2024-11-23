import math

def getNucelotideProb(gcProb):
    probA = (1-gcProb)/2
    probT = probA
    probG = gcProb/2
    probC = probG
    probNuc = {'A':probA, 'T':probT, 'G':probG, 'C':probC}
    return probNuc

if __name__ == '__main__':
    fileInput='input.txt'
    with open(fileInput, 'r') as fr:
        reading=fr.readlines()
        arrayA = reading[0].strip()
        gcProbCases = map(float, reading[1].strip().split(" "))

    answer=list()
    for gcProb in gcProbCases:
        probNuc = getNucelotideProb(gcProb)
        
        totalProb=1
        for nuc in arrayA:
            prob = probNuc[nuc]
            totalProb*=prob
        logProb=math.log10(totalProb)
        roundProb=round(logProb,3)
        answer.append(roundProb)
    
    print(*answer)