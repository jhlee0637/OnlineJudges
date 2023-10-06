'''
https://leetcode.com/problems/product-of-array-except-self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    - Input: nums = [1,2,3,4]
    - Output: [24,12,8,6]

Example 2:
    - Input: nums = [-1,1,0,-3,3]
    - Output: [0,0,9,0,0]
'''
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


'''
틀린풀이: 문제에서 요구하는 O(n)을 충족시키지 못함.
         이후에 1로 만들어진 리스트를 따로 만들어서 시작한다는 생각은 했으나
         각 요소의 모든 왼쪽 요소를 먼저 곱하고, 그 다음에는 오른쪽 요소를 곱한다는 분리된 생각은 하지 못함.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(0, len(nums)):
            multi=1
            for j in range(0, len(nums)):
                if j!=i:
                    multi*=nums[j]
            result.append(multi)
        return result
'''