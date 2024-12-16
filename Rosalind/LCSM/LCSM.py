def getSeq(filename):
    nameSeq=dict()
    with open(filename, 'r') as fr:
        reading=fr.readlines()
        for line in reading:
            line=line.strip()
            if line.startswith('>'):
                name=line
                nameSeq[name]=''
            else:
                nameSeq[name]+=line
    return nameSeq.values()

def getLongestCommonSubString(onlySeqs):
    longestSubStr=''
    onlySeqs = list(onlySeqs)
    if len(onlySeqs) > 1:
        frstSeq=onlySeqs[0] #using the first sequence only to compare <- potential problem. What if it is NNNNNN
        if len(frstSeq)>0:
            for i in range(len(frstSeq)):
                for j in range(len(frstSeq) - i + 1):
                    if j>len(longestSubStr):
                        flag=1
                        for seq in onlySeqs:
                            if frstSeq[i:i+j] in seq:
                                pass
                            else:
                                flag=0
                                break
                        if flag==1:
                            longestSubStr = frstSeq[i:i+j]
    return longestSubStr

if __name__=="__main__":
    filename="input.txt"
    seq = getSeq(filename)
    print(getLongestCommonSubString(seq))