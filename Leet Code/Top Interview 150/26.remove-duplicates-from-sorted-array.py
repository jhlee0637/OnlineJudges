#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for each in nums:
            numOfEach=nums.count(each)
            for i in range(1, numOfEach):
                nums.remove(each)
        k=len(nums)
# @lc code=end

