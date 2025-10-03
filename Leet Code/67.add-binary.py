#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_a = 0
        for i in range(len(a)):
            n = int(a[i])
            dec_a += n*(2**(len(a)-1-i))

        dec_b = 0
        for i in range(len(b)):
            n = int(b[i])
            dec_b += n*(2**(len(b)-1-i))

        dec_sum = dec_a + dec_b
        bi_sum = ''
        if dec_sum==0:
            bi_sum='0'
        elif dec_sum==1:
            bi_sum='1'
        else:
            while True:
                quo = dec_sum//2
                bi_sum+=str(dec_sum%2)
                if quo==1 or quo==0:
                    bi_sum+=str(quo)
                    break
                else:
                    dec_sum = quo
        return bi_sum[::-1]

        
# @lc code=end

