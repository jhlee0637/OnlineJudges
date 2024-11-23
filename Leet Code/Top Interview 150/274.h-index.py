#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=sorted(citations, reverse=True)
        cnt=0
        for i in range(0, len(citations)):
            val=citations[i]
            if val>=cnt+1:
                cnt+=1
            else:
                break
        return cnt        
# @lc code=end

