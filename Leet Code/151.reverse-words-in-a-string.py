#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        string=[line for line in s.strip().split(" ")[::-1] if len(line)!=0]
        space = [" " for i in range(len(string)-1)]
        answer=string[0]
        for string, space in  zip(string[1:], space):
            answer+=space
            answer+=string
        return answer
# @lc code=end

