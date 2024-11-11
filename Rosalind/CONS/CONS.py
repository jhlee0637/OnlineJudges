def getSeqOnly(input):
    seqs=list()
    seq=''
    with open(input, "r") as fr:
        reading=fr.readlines()
        for line in reading:
            line=line.strip()
            if line.startswith('>') is True:
                seqs.append(seq)
                seq=''
            elif line==reading[-1].strip():
                seq+=line
                seqs.append(seq)
            else:
                seq+=line
    i=len(seqs[-1])
    return seqs[1:], i

def countN(seqs, i):
    countA=[0 for j in range(0, i)]
    countC=[0 for j in range(0, i)]
    countG=[0 for j in range(0, i)]
    countT=[0 for j in range(0, i)]
    for seq in seqs:
        for k in range(len(seq)):
            if seq[k]=="A":
                countA[k]+=1
            if seq[k]=="C":
                countC[k]+=1
            if seq[k]=="G":
                countG[k]+=1
            if seq[k]=="T":
                countT[k]+=1
    return countA, countC, countG, countT



if __name__=='__main__':
    input='input.txt'

    seqs, i=getSeqOnly(input)
    countA, countC, countG, countT = countN(seqs, i)

    best=list()
    nuc=["A", "C", "G", "T"]
    for k in range(len(countA)):
        cntK=[countA[k], countC[k], countG[k], countT[k]]
        highScore=max(cntK)
        best.append(nuc[cntK.index(highScore)])
        
    print(''.join(best))
    print(f"A: {' '.join(map(str, countA))}")
    print(f"C: {' '.join(map(str, countC))}")
    print(f"G: {' '.join(map(str, countG))}")
    print(f"T: {' '.join(map(str, countT))}")    