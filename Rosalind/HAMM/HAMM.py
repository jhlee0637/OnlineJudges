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