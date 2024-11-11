'''
https://rosalind.info/problems/revc/

Problem: In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
         The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol
         (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset: AAAACCCGGT
Sample Output:  ACCGGGTTTT
'''

def convertDNAtoComp(seq, compRule):
    compSeq=""
    for n in seq:
        oldN=n
        newN=compRule.get(n, oldN)
        compSeq+=newN
    compSeq=compSeq[::-1]
    return compSeq

if __name__ == "__main__":
    compRule={"A":"T", "T":"A", "G":"C", "C":"G"}
    seq="AAAACCCGGT"
    #seq=""
    
    complementarySeq=convertDNAtoComp(seq, compRule)
    print (complementarySeq)
    