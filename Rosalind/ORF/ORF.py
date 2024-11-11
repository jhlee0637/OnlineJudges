"""
https://rosalind.info/problems/orf/

Problem: Either strand of a DNA double helix can serve as the coding strand for RNA transcription.

Hence, a given DNA string implies six total reading frames,
or ways in which the same region of DNA can be translated into amino acids:
three reading frames result from reading the string itself,
whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon,
without any other stop codons in between.

Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s.
        Strings can be returned in any order.

Sample Dataset: >Rosalind_99
                AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output: MLLGSFRLIPKETLIQVAGSSPCNLS
               M
               MGMTPRLGLESLLE
               MTPRLGLESLLE
"""

def getCodon():
    codonProtein={'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
                  'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
                  'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
                  'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
                  'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
                  'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
                  'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
                  'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
                  'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
                  'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
                  'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
                  'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
                  'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
                  'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
                  'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
                  'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}
    return codonProtein

def getSeq(file_name):
    rule={'A':'T','T':'A','G':'C', 'C':'G'}
    with open(file_name, 'r') as fr:
        head=fr.readline()
        seq=''
        rev_seq=''

        reading=fr.readlines()
        for line in reading:
            line=line.strip()
            seq+=line
            for s in seq:
                rev_seq+=rule[s]
        
        rev_seq=rev_seq[::-1] #3'-5' > 5'-3'
        return seq, rev_seq

def getORF(seq, codons):
    proteins=list()
    for i in range(0,3):
        flag=False
        protein=''
        for j in range(i, len(seq),3):

            is_codon=seq[j:j+3]
            if len(is_codon)==3:
                codon=codons[is_codon]
                #print(i, flag, codon, protein)
                if flag==False and codon=='M':
                    flag=True
                    protein='M'
                elif flag==True and codon!='Stop':
                    protein+=codon
                elif flag==True and codon=='Stop':
                    flag=False
                    if protein.count('M')>1:
                        m_position=list()
                        for pi in range(len(protein)):
                            if protein[pi]=='M':
                                m_position.append(pi)
                        for pos in m_position:
                            proteins.append(protein[pos:])
                    else:
                        proteins.append(protein)
                    protein=''
    
    return proteins
                
if __name__ == "__main__":
    codons=getCodon()
    DNA_1, DNA_2=getSeq('input.txt')
    r1=getORF(DNA_1, codons)
    r2=getORF(DNA_2, codons)
    for s in set(r1+r2):
        print(s)
