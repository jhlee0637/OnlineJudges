'''
https://leetcode.com/problems/jump-game/description

You are given an integer array nums.
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
    - Input: nums = [2,3,1,1,4]
    - Output: true
    - Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

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