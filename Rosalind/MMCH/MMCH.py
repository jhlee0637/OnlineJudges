with open('input.txt', 'r') as fr:
    reading=fr.readlines()
    seq=''
    for line in reading:
        if line.startswith(">"):
            pass
        else:
            line=line.strip()
            seq+=line
    
dic_nuc={'A':'U', 'U':'A', 'G':'C', 'C':'G'}

c=0
if len(seq)%2!=0:
    c=len(seq)//2
else:
    c=(len(seq)//2)+1

cnt=0
for i in range(c+1):
    for j in range(c+1,len(seq)):
        A = seq[i]
        B = seq[j]
        if dic_nuc[A]==B:
            cnt+=1

val=1
for i in range(1, cnt+1):
    val*=i
print(val)