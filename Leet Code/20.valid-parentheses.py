# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s):
        stack = list() # 스택 안에는 닫힘 꺽쇠만 넣을 것이다.
        brackets = {"{":"}", "(":")", "[":"]"}
        for c in s:
            # 스택에 '닫힘 꺽쇠'를 넣어야하는 경우
            #   1) 열림 꺽쇠일 때
            if c in brackets.keys():
                    stack.append(brackets[c])
            # 닫힘꺽쇠를 뽑았다면, 스택에서 꺼낸 값과 같아야한다
            else:
                 if len(stack)==0 or stack.pop() != c :
                      return False
        if len(stack)!=0:
            return False
        else:
            return True


                

            

# @lc code=end