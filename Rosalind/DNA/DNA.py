def countNucleotide(string):
    dic_NT=dict()
    for NT in string:
        dic_NT[NT]=dic_NT.get(NT, 0)+1
    return dic_NT

seq="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#seq=""

dic_input=countNucleotide(seq)
print (dic_input["A"], dic_input["C"], dic_input["G"], dic_input["T"])