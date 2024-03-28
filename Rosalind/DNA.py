'''
https://rosalind.info/problems/dna/

Problem: A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
         An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Sample Output:  20 12 17 21
'''
def countNucleotide(string):
    dic_NT=dict()
    for NT in string:
        dic_NT[NT]=dic_NT.get(NT, 0)+1
    return dic_NT

seq="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#seq=""

dic_input=countNucleotide(seq)
print (dic_input["A"], dic_input["C"], dic_input["G"], dic_input["T"])