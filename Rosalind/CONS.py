'''
https://rosalind.info/problems/cons/

Problem: A matrix is a rectangular table of values divided into rows and columns.
         An m×n matrix has m rows and n columns.
         Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

         Say that we have a collection of DNA strings, all having the same length n.
         Their profile matrix is a 4×n matrix P in which,
         P1,j represents the number of times that 'A' occurs in the jth position of one of the strings,
         P2,j represents the number of times that C occurs in the jth position, and so on (see below).

         A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position;
         the jth symbol of c therefore corresponds to the symbol having the maximum value in the jth column of the profile matrix.

         Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

DNA Strings: A T C C A G C T
             G G G C A A C T
             A T G G A T C T
             A A G C A A C C
             T T G G A A C T
             A T G C C A T T
             A T G G C A C T

Profile:     A   5 1 0 0 5 5 0 0
             C   0 0 1 4 2 0 6 1
             G   1 1 6 3 0 1 0 0
             T   1 5 0 0 0 1 1 6

Consensus:	 A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection
        (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset: >Rosalind_1
                ATCCAGCT
                >Rosalind_2
                GGGCAACT
                >Rosalind_3
                ATGGATCT
                >Rosalind_4
                AAGCAACC
                >Rosalind_5
                TTGGAACT
                >Rosalind_6
                ATGCCATT
                >Rosalind_7
                ATGGCACT

Sample Output:  ATGCAACT
                A: 5 1 0 0 5 5 0 0
                C: 0 0 1 4 2 0 6 1
                G: 1 1 6 3 0 1 0 0
                T: 1 5 0 0 0 1 1 6
'''
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