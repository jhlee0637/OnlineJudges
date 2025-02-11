#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaLow = [chr(i) for i in range(97, 123)]
        alphaLow += [str(i) for i in range(0,10)]

        onlyChr=''
        for c in s:
            c = c.strip().lower()
            if c in alphaLow:
                onlyChr += c.strip().lower()

        i=0
        answer=True
        while True:
            if i == len(onlyChr)//2:
                break
            else:
                if onlyChr[i]==onlyChr[-i-1]:
                    i+=1
                    continue
                else:
                    answer=False
                    break

        return answer
    
        
# @lc code=end

