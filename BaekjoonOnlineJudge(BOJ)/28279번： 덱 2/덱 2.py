#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28279                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28279                          #+#        #+#      #+#     #
#    Solved: 2025/01/30 13:12:51 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

class DeckTwo():
    def __init__(self):
        self.q = deque()

    def addFront(self, X):
        self.q.appendleft(X)

    def addBack(self, X):
        self.q.append(X)

    def popFront(self):
        if len(self.q)>0:
            return self.q.popleft()
        else:
            return -1
        
    def popBack(self):
        if len(self.q)>0:
            return self.q.pop()
        else:
            return -1
    
    def getLength(self):
        return len(self.q)
    
    def checkEmpty(self):
        if len(self.q)==0:
            return 1
        else:
            return 0
        
    def getFront(self):
        if len(self.q)>0:
            return self.q[0]
        else:
            return -1
        
    def getBack(self):
        if len(self.q)>0:
            return self.q[-1]
        else:
            return -1


reading=sys.stdin.readlines()

deck=DeckTwo()
for line in reading[1:]:
    try:
        cmd, i=list(map(int, line.strip().split(" ")))
        if cmd==1:
            deck.addFront(i)
        elif cmd==2:
            deck.addBack(i)
    except:
        cmd=int(line.strip())
        if cmd==3:
            answer=deck.popFront()
        elif cmd==4:
            answer=deck.popBack()
        elif cmd==5:
            answer=deck.getLength()
        elif cmd==6:
            answer=deck.checkEmpty()
        elif cmd==7:
            answer=deck.getFront()
        elif cmd==8:
            answer=deck.getBack()
        else:
            KeyError()
            break
        print(answer)
        
'''
Class 및 deque를 이용한 구현
deque의 경우 pop() 함수가 list class의 pop(n)보다 시간복잡도 측면에서 우위이다 (O(1) vs O(n))
'''