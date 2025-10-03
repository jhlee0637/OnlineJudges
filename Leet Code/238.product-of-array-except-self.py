#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize left and right product arrays
        left_products = [1] * n
        right_products = [1] * n
        
        # Calculate left products
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
        
        # Calculate right products
        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        # Calculate the final answer
        answer = [left_products[i] * right_products[i] for i in range(n)]
        
        return answer

# @lc code=end

