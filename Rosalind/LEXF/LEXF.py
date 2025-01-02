with open('input.txt', 'r') as fr:
    reading=fr.readlines()
    seq = reading[0].strip().split(" ")
    n = int(reading[1].strip())

def recursiveCombo(n, s):
    if len(s)==n:
        print(s)
    else:
        for e in seq:
            recursiveCombo(n, s+e)

for s in seq:
    recursiveCombo(n, s)