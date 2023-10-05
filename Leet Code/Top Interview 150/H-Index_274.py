'''
https://leetcode.com/problems/h-index/

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:
    - Input: citations = [3,0,6,1,5]
    - Output: 3
    - Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
                   Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
    - Input: citations = [1,3,1]
    - Output: 1

Answer reference: https://algo.monster/liteproblems/274
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=sorted(citations, reverse=True)
        cnt=0
        for i in range(0, len(citations)):
            val=citations[i]
            if val>=cnt+1:
                cnt+=1
            else:
                break
        return cnt
    
'''
틀린풀이

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        array=citations
        array=sorted(array, reverse=True)
        strt=len(array)
        maxVal=max(array)
       # zero situation
        if array[0]==0:
            return 0
            exit
        # single array situation
        if strt==1:
            return 1
            exit
        # else
        idxStrt=array.index(strt)
        for i in range(idxStrt, len(array)):
            lenDue=idxStrt+i
            val=array[i]
            print(i, lenDue, val)
            if lenDue==val:
                return val
                
input이 무의미하게 길어지는 경우를 대비해서 index를 찾는 시작지점(idxStrt)를 리스트의 중간에서 찾으려는 시도를 했다.
그러나 이러한 판단은 문제의 핵심을 빗나간 판단이었다.
'''