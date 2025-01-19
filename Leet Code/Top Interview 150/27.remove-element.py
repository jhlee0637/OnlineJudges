#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val)>0:
            nums.remove(val)
        k=len(nums)
# @lc code=end

