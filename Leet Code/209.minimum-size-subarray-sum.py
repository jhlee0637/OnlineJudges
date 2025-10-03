#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer=float('inf')
        l=0
        r=0
        checkSum=sum(nums[l:r])
        while r<len(nums):
            checkSum+=nums[r]
            r+=1
            while checkSum>=target:
                answer=min(answer, r-l)
                checkSum-=nums[l]
                l+=1

        return 0 if answer == float('inf') else answer

        
# @lc code=end

