def getLineSeq(file):
    lineSeq=dict()
    with open(file, 'r') as fr:
        reading=fr.readlines()
        seqName=''
        seq=''
        for i in range(len(reading)):
            line=reading[i].strip()
            if line.startswith(">"):
                lineSeq[seqName]=seq
                seqName=line[1:]
                seq=''
            elif i+1==len(reading):
                seq+=line
                lineSeq[seqName]=seq
            else:
                seq+=line
    return lineSeq

def getGCPrct(name, seq):
    denom=0.0
    num=0.0
    for s in seq:
        if s=="G" or s=="C":
            denom+=1
            num+=1
        else:
            num+=1
    if num!=0:
        GCPrct=float(denom/num)*100
    else:
        GCPrct=0
    return name, GCPrct


if __name__=="__main__":
    inputFile="input.txt"

    lineSeq=getLineSeq(inputFile)

    bestName=''
    bestPrct=0.0
    for name_seq in sorted(lineSeq.items()):
        name, GCPrct = getGCPrct(name_seq[0], name_seq[1])
        if GCPrct>bestPrct:
            bestName=name
            bestPrct=GCPrct
            
    print(bestName)
    print(bestPrct)

    
    