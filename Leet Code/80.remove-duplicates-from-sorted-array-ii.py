#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dicFlag=dict()
        lenOriginal=len(nums)
        copyNums=[x for x in nums]
        for i in range(0, lenOriginal):
            element=copyNums[i]
            flagCheck=dicFlag.get(element, 0)
            if flagCheck==0:
                dicFlag[element]=1
                pass
            elif flagCheck==1:
                dicFlag[element]=2
                pass
            else:
                nums.remove(element)
            print(i, copyNums, nums)
# @lc code=end

