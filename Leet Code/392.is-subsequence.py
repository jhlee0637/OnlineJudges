#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        idx=0
        answer=False
        while True:
            if t=="" and s!="":
                break

            elif len(s)==i:
                answer=True
                break

            else:
                target = s[i]
                try:
                    idx += t[idx:].index(target) + 1
                    i+=1
                except:
                    break

        return answer

# @lc code=end

