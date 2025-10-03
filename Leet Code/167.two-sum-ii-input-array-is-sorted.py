#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer=False
        i=0
        j=0
        while True:
            j+=1
            if numbers[i]+numbers[j]==target:
                answer=[i+1, j+1]
                break
            else:
                if numbers[i]==numbers[j]: #at the early of array, it happens
                    i+=1
                    j=i
                elif j==len(numbers)-1: #at the end of array, reset
                    i+=1
                    j=i
                elif numbers[i]+numbers[j]>target: #quick reset
                    i+=1
                    j=i
        return answer

'''
It's not a good solution. Time Complexity is O(n^2) maximumly
Best solution should use Two-pointer system properly.
'''            
        
# @lc code=end

