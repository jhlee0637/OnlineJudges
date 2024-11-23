def getSeqItems(file):
    with open(file, 'r') as fr:
        head=fr.readline().strip()[1:]
        seq=''
        seqItems={head:seq}
        reading=fr.readlines()
        for i in range(len(reading)):
            line=reading[i].strip()
            if line.startswith(">"):
                seqItems[head]=seq
                head=line[1:]
                seq=''
            elif i+1==len(reading):
                seq+=line
                seqItems[head]=seq
            else:
                seq+=line
    return seqItems.items()

def compareSeq(front, back, k):
    '''
    Compare k-length of last sequences of 'front' with first sequences of 'back'

    If k-length of the seqeunces are equal, return True
    
    If k is longer than the length of two given sequnces, return error 
    '''
    if k > len(front) or k>len(back):
        raise ValueError("k is longer than sequence")
    
    seqFront=front[-k:]
    seqBack=back[:k]

    if seqFront==seqBack:
        return True
    else:
        return False

if __name__ == "__main__":
    k=3
    seqItems=list(getSeqItems('input.txt'))
    for i in range(len(seqItems)):
        for j in range(len(seqItems)):
            if i!=j:
                front=seqItems[i][1]
                back=seqItems[j][1]
                if compareSeq(front, back, k) == True:
                    print(seqItems[i][0], seqItems[j][0])