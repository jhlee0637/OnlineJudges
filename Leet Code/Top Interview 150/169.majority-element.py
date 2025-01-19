#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic_count=dict()
        for element in nums:
            dic_count[element]=dic_count.get(element, 0)+1
        return sorted(dic_count.items(), key=lambda X : X[1], reverse=True)[0][0]     
# @lc code=end

