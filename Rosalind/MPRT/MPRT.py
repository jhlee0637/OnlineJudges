"""
Problem: To allow for the presence of its varying forms,
         a protein motif is represented by a shorthand as follows:
         [XY] means "either X or Y" and {X} means "any amino acid except X."
         
         For example, the N-glycosylation motif is written as N{P}[ST]{P}.
         
         You can see the complete description and features of a particular protein
         by its access ID "uniprot_id" in the UniProt database,
         by inserting the ID number into http://www.uniprot.org/uniprot/uniprot_id

         Alternatively, you can obtain a protein sequence in FASTA format by following 
         http://www.uniprot.org/uniprot/uniprot_id.fasta

         For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif,
        output its given access ID followed by a list of locations
        in the protein string where the motif can be found.

Sample Dataset: A2Z669
                B5ZC00
                P07204_TRBM_HUMAN
                P20840_SAG1_YEAST

Sample Output: B5ZC00
               85 118 142 306 395
               P07204_TRBM_HUMAN
               47 115 116 382 409
               P20840_SAG1_YEAST
               79 109 135 248 306 348 364 402 485 501 614
"""
import wget
import os

def getProteinSeq(filename):
    prtSeq = dict()

    with open(filename, 'r') as fr:
        reading=fr.readlines()
        for line in reading:
            prtName=line.strip()
            FASTAfilename = prtName + ".fasta"
            if "_" in prtName:
                FASTAfilename=prtName.split("_")[0] + ".fasta"
            urlFasta = "http://www.uniprot.org/uniprot/" + FASTAfilename

            if FASTAfilename in os.listdir(os.getcwd()):
                pass
            else:
                wget.download(urlFasta)

            with open(FASTAfilename, 'r') as frfasta:
                seq = ""
                frfasta.readline()
                readingfasta = frfasta.readlines()
                for fastaline in readingfasta:
                    fastaline=fastaline.strip()
                    seq+=fastaline

            prtSeq[prtName] = seq

    return prtSeq

def getMotifLoc(sequence):
    '''
    We are looking for N-linked glycosylation site  where the next three protiens are
    1. N X S X (X is any amino acid except proline)
    2. N X T X (X is any amino acid except proline)
    '''
    locNXSTX=list()
    for i in range(len(sequence)):
        if sequence[i] == "N" and i+3<len(sequence):
            if sequence[i+2]=="S" or sequence[i+2]=="T":
                if sequence[i+1]!="P" and sequence[i+3]!="P":
                    locNXSTX.append(i+1) #zero base
    locNXSTX=map(str, locNXSTX)
    return locNXSTX

if __name__ == "__main__":
    prtSeq = getProteinSeq("input.txt")
    print("---")
    for prt in prtSeq.items():
        prtName = prt[0]
        prtSeq = prt[1]
        motifLoc = getMotifLoc(prtSeq)
        motifLoc = " ".join(motifLoc)
        if len(motifLoc)!=0:
            print (prtName)
            print (motifLoc)