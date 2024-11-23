def getProtein(codon):
    codonProtein={'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
                  'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
                  'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
                  'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
                  'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
                  'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
                  'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
                  'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
                  'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
                  'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
                  'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
                  'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
                  'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
                  'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
                  'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
                  'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G' }
    protein=codonProtein[codon]
    return protein

codonList=list()
if __name__ == "__main__":
    with open ('input.txt', 'r') as fr:
        reading=fr.readlines()
        s=''
        for i in range(1, len(reading)):
            line=reading[i].strip()
            if line.startswith(">")==False:
                s+=line
            elif line.startswith(">")==True:
                intronStart=i
                break
        for line in reading[intronStart:]:
            if line.startswith(">")==False:
                intron=line.strip()
                intronIndex=s.index(intron)
                s=s[:intronIndex]+s[intronIndex+len(intron):]
                
    transcription=False
    rnaExon=s.replace("T", "U")
    codon=''
    answer=''
    for n in rnaExon:
        codon+=n
        if len(codon)==3:
            prt=getProtein(codon)
            if prt=='M':
                transcription=True
            elif prt=='Stop':
                transcription=False
            if transcription==True:
                answer+=prt
            codon=''
print(answer)