# Return complement sequence of a given sequence
def getCompSeq(seq):
    comp={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    compSeq=''
    for s in seq:
        compSeq+=comp[s]
    return compSeq
            
if __name__ == "__main__":
    # Read file
    with open('input.txt', 'r') as fr:
        reading=fr.readlines()
        seq=''
        for line in reading[1:]:
            line=line.strip()
            seq+=line
    
    # Solution 1. Brutal Force
    # From every index of the sequence, search the longest sequence which is same with the reversed complement sequence
    for i in range(len(seq)):
        for j in range(4,13):
            # Range should not over the given sequence length
            if i+j>len(seq):
                pass
            else:
                testSeq = seq[i:i+j]

                # Get reversed complement sequence
                compSeq=getCompSeq(testSeq)
                revCompSeq=compSeq[::-1]

                # Compare the result
                if revCompSeq==testSeq:
                    # Index is Zero based
                    print(i+1, j)
                else:
                    continue