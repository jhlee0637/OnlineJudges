with open('input.txt', 'r') as fr:
    reading=fr.readlines()
    
    # Given value N
    n = int(reading[0].strip())
    
    # Given nodes' information
    nodes = [line.strip() for line in reading[1:]]

# How many edges we need? = total nodes - 1
m = n-1

# How many edges we have? = len(nodes)
e = len(nodes)

# Answer = edges we have - edges we need
print(m-e)


'''
복잡한 문제라고 생각하고 접근하였으나 아니였음

###참고
- http://saradoesbioinformatics.blogspot.com/2016/08/completing-tree.html
'''