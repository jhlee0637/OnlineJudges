'''
https://rosalind.info/problems/hamm/

Problem: Given two strings s and t of equal length,the Hamming distance between s and t,
         denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
         See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset: GAGCCTACTAACGGGAT
                CATCGTAATGACGGCCT

Sample Output:  7
'''

if __name__=='__main__':
    seq_1='GAGCCTACTAACGGGAT'
    seq_2='CATCGTAATGACGGCCT'
    #seq_1=''
    #seq_2=''
    count=0
    for a, b in zip(seq_1, seq_2):
        if a!=b:
            count+=1
    print(count)