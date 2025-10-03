#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #t: O(NlogN)
        answer=list()
        for i in range(len(nums)-2): #t: O(N)
            l = i #left <- fixed
            m = i+1 #middle <- two pointer, point 1
            r = len(nums)-1 #right <- two pointer, point 2

            if l>0 and nums[l-1]==nums[l]:
                continue #duplicate check l
            else:
                while l<m<r<len(nums): #O(N) * O(N) = O(N^2)
                    t = [nums[l], nums[m], nums[r]]      
                    if sum(t)==0: #sum==0
                        answer.append(t)
                        m+=1 #update m
                        r-=1 #update r
                        while nums[m] == nums[m-1] and m<r: #duplicate check m 
                            m+=1
                        while nums[r] == nums[r+1] and m<r: #duplicate check r 
                            r-=1
                    elif sum(t)<0: #less than 0 -> update m
                        m+=1
                    elif sum(t)>0: #larger than 0 -> update r
                        r-=1
        return answer

'''
time complexity: O(NlogN + N^2) -> O(N^2)
'''
# @lc code=end

