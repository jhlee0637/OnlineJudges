'''
https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    - Input: nums = [1,2,3,4,5,6,7], k = 3
    - Output: [5,6,7,1,2,3,4]
    - Explanation:
                    rotate 1 steps to the right: [7,1,2,3,4,5,6]
                    rotate 2 steps to the right: [6,7,1,2,3,4,5]
                    rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            nums.insert(0, nums[-1])
            nums.pop()