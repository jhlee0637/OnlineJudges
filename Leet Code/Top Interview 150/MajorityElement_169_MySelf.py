'''
August. 2023
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
    - Input: nums = [3,2,3]
    - Output: 3
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic_count=dict()
        for element in nums:
            dic_count[element]=dic_count.get(element, 0)+1
        return sorted(dic_count.items(), key=lambda X : X[1], reverse=True)[0][0]