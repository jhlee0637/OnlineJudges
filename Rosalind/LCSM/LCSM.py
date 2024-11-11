'''
https://rosalind.info/problems/lcsm/

Problem: A common substring of a collection of strings is
         a substring of every member of the collection. We
         say that a common substring is a longest common
         substring if there does not exist a longer common
         substring. For example, "CG" is a common substring
         of "ACGTACGT" and "AACCGTATA", but it is not as
         long as possible; in this case, "CGTA" is a longest
         common substring of "ACGTACGT" and "AACCGTATA".
         
         Note that the longest common substring is not necessarily
         unique; for a simple example, "AA" and "CC" are
         both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at
       most 1 kbp each in FASTA format.

Return: A longest common substring of the collection.
        (If multiple solutions exist, you may return any single solution.)

Sample Dataset: >Rosalind_1
                GATTACA
                >Rosalind_2
                TAGACCA
                >Rosalind_3
                ATACA

Sample Output:  AC
'''
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