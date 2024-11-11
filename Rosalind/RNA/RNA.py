'''
https://rosalind.info/problems/rna/

Problem: An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
         Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.

Sample Dataset: GATGGAACTTGACTACGTAAATT
Sample Output: GAUGGAACUUGACUACGUAAAUU
'''
def convertDNAtoRNA(seq, RNAstring):
    RNAseq=""
    for n in seq:
        oldN=n
        newN=RNAstring.get(n, oldN)
        RNAseq+=newN
    return RNAseq

if __name__ == "__main__":
    RNAstring={"T":"U"}
    seq="GATGGAACTTGACTACGTAAATT"
    #seq=""
    
    RNAseq=convertDNAtoRNA(seq, RNAstring)
    print (RNAseq)
    
