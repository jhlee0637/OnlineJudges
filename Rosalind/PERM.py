'''
https://rosalind.info/problems/perm/

Problem: A permutation of length n is an ordering of the positive integers {1,2,…,n}.
         For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset: 3

Sample Output:  6
                1 2 3
                1 3 2
                2 1 3
                2 3 1
                3 1 2
                3 2 1
'''

def getPermutation(nums, result, limit):
    if len(nums) == 0:
        yield result
    elif len(result) == limit:
        yield result
    else:
        for i in range(len(nums)):
            yield from getPermutation(nums[:i] + nums[i + 1:], result + [nums[i]], limit)

if __name__ == '__main__':
    i = 3
    #i=

    cnt=1
    nums=list()
    for i in range(1, i + 1):
        nums.append(i)
        cnt=cnt*i
    print (cnt)
    
    result = list()
    for p in getPermutation(nums, result, i):
        print(' '.join(map(str,p)))
