#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        answer=""
        s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        v = [1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1]
        for i in range(len(v)):
            val = v[i]
            a = num//val
            if a!=0:
                answer+=a*s[i]
            num-=a*val
        return answer



# @lc code=end

