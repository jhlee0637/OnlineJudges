#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
                        "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900} #S: O(1)

        val=0
        skipFlag=False
        for i in range(len(s)-1): #T: O(n)
            if skipFlag is True:
                skipFlag=False
                pass
            else:
                oneS = s[i]
                twoS = s[i:i+2]
                if symbol_value.get(twoS, False) is not False:
                    val+=symbol_value[twoS]
                    skipFlag=True
                else:
                    val+=symbol_value[oneS]

        if skipFlag is False:
            val+=symbol_value[s[-1]]
            
        return(val)
        
# @lc code=end

#Time complexity: O(n)
#Space complexity: O(1) 