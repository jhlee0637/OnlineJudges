#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs.count("")>0:
            return ""
            exit

        lengths = [len(s) for s in strs]
        minL = min(lengths)
        
        i=0
        while True:
            i+=1
            if i > minL:
                break
            else:
                target=""
                for s in strs:
                    try:
                        if target=="":
                            target=s[:i]
                        else:
                            compare=s[:i]
                            if target==compare:
                                continue
                            else:
                                target=target[:-1] #false > go back
                                i+=minL #while loop break
                                break
                    except:
                        break
        return target
        
# @lc code=end

