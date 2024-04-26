'''
https://rosalind.info/problems/grph/

Problem: A graph whose nodes have all been labeled can be represented by an adjacency list,
         in which each row of the list contains the two node labels corresponding to a unique edge.
         
         A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation.

         That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively.

         The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)).
          
         A directed loop is a directed edge of the form (v,v).

         For a collection of strings and a positive integer k,
         the overlap graph for the strings is a directed graph Ok in which each string is represented by a node,
         and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t,
         as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3.
        You may return edges in any order.

Sample Dataset: >Rosalind_0498
                AAATAAA
                >Rosalind_2391
                AAATTTT
                >Rosalind_2323
                TTTTCCC
                >Rosalind_0442
                AAATCCC
                >Rosalind_5013
                GGGTGGG

Sample Output: Rosalind_0498 Rosalind_2391
               Rosalind_0498 Rosalind_0442
               Rosalind_2391 Rosalind_2323
'''

def getSeqItems(file):
    with open(file, 'r') as fr:
        head=fr.readline().strip()[1:]
        seq=''
        seqItems={head:seq}
        reading=fr.readlines()
        for i in range(len(reading)):
            line=reading[i].strip()
            if line.startswith(">"):
                seqItems[head]=seq
                head=line[1:]
                seq=''
            elif i+1==len(reading):
                seq+=line
                seqItems[head]=seq
            else:
                seq+=line
    return seqItems.items()

def compareSeq(front, back, k):
    '''
    Compare k-length of last sequences of 'front' with first sequences of 'back'

    If k-length of the seqeunces are equal, return True
    
    If k is longer than the length of two given sequnces, return error 
    '''
    if k > len(front) or k>len(back):
        raise ValueError("k is longer than sequence")
    
    seqFront=front[-k:]
    seqBack=back[:k]

    if seqFront==seqBack:
        return True
    else:
        return False

if __name__ == "__main__":
    k=3
    seqItems=list(getSeqItems('input.txt'))
    for i in range(len(seqItems)):
        for j in range(len(seqItems)):
            if i!=j:
                front=seqItems[i][1]
                back=seqItems[j][1]
                if compareSeq(front, back, k) == True:
                    print(seqItems[i][0], seqItems[j][0])