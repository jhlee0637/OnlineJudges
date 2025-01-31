#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18115                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18115                          #+#        #+#      #+#     #
#    Solved: 2025/01/31 16:26:53 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

class skill():
    def __init__(self):
        self.q=deque()
    
    def getDeque(self):
        return list(self.q)

    def addLeft(self, i):
        self.q.appendleft(i)
    
    def addSecond(self, i):
        topLeft = self.q.popleft()
        self.addLeft(i)
        self.addLeft(topLeft)
        
    def addRight(self, i):
        self.q.append(i)
    
N=int(sys.stdin.readline().strip())
A=list(map(int, sys.stdin.readline().strip().split(" ")))

A=A[::-1] #reversed skills order 
nums = range(1,N+1)

answer=skill()
for i in range(N):
    x = A[i] #skill
    n = nums[i] #card
    if x==1:
        answer.addLeft(n)
    elif x==2:
        answer.addSecond(n)
    elif x==3:
        answer.addRight(n)

print(*answer.getDeque())

'''
Class와 collection library를 이용한 deque 구현
'''