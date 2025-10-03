#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        answer=['' for i in range(numRows)]
        if numRows==1 or len(s)==1:
            answer=s
        else:
            while len(s)>0:
                for i in range(numRows):
                    if len(s)>0:
                        answer[i]+=s[0]
                        s=s[1:]
                    else:
                        break

                for i in range(1, numRows-1):
                    if len(s)>0:
                        answer[numRows-1-i]+=s[0]
                        s=s[1:]
                    else:
                        break

        answer=''.join(answer)
        return answer
                
# @lc code=end

