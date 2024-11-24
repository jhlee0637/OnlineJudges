with open('input.txt', 'r') as fr:
    reading=fr.readline()

    # Given n and k
    n, k = map(int, reading.strip().split(' '))

# Calculate total permutation
totalPermutation=1
for i in range(k):
    totalPermutation=totalPermutation*n
    n=n-1

# Calculate modulo 1M
answer=totalPermutation%1000000
print(answer)