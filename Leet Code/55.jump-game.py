#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        answer=True
        maxIdx=0
        for idx in range(0, len(nums)):
            val=nums[idx]
            nextIdx=idx+val
            maxIdx=max(maxIdx, nextIdx)
            if nextIdx>=(len(nums)-1):
                #reach to end
                break
            elif val==0 and maxIdx<=idx:
                answer=False
                break
        return answer 
        
# @lc code=end

