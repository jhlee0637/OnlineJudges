def getNucelotideProb(gcProb):
    probA = (1-gcProb)/2
    probT = probA
    probG = gcProb/2
    probC = probG
    return probA, probT, probG, probC

if __name__ == '__main__':
    fileInput='input.txt'
    with open(fileInput, 'r') as fr:
        reading=fr.readlines()
        stringLength = int(reading[0].strip())
        arrayA = reading[1].strip()
        gcProbCases = map(float, reading[2].strip().split(" "))
  
    answer=list()
    nucChance=stringLength-len(arrayA)+1
    for gcProb in gcProbCases:
        probA, probT, probG, probC = getNucelotideProb(gcProb)
        totalProb=1
        for nuc in arrayA:
            if nuc=="A":
                totalProb*=probA
            elif nuc=="T":
                totalProb*=probT
            elif nuc=="G":
                totalProb*=probG
            elif nuc=="C":
                totalProb*=probC
            else:
                print("Error")
                break
        answer.append(round(nucChance*totalProb,3))
    
    print(*answer)
    