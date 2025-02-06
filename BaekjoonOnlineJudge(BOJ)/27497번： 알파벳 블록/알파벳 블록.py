#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 27497                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/27497                          #+#        #+#      #+#     #
#    Solved: 2025/02/06 15:03:12 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

class game():
    def __init__(self):
        self.q = deque()

    def addBack(self, c):
        self.q.append(c)

    def addFront(self, c):
        self.q.appendleft(c)

    def removeBack(self):
        self.q.pop()

    def removeFront(self):
        self.q.popleft()
    
    def getArray(self):
        return self.q

reading=sys.stdin.readlines()

answer=game()
cmdList=list()
for line in reading[1:]:
    line=line.strip().split(" ")
    cmd = int(line[0])
    if len(line)==2:
        character = line[1]
        if cmd==1:
            answer.addBack(character)
            cmdList.append(cmd)
        elif cmd==2:
            answer.addFront(character)
            cmdList.append(cmd)
    else: #cmd==3
        if len(cmdList)>0:
            prevCmd=cmdList.pop()
            if prevCmd==1:
                answer.removeBack()
            elif prevCmd==2:
                answer.removeFront()

if len(answer.getArray())==0:
    print(0)
else:
    print("".join(list(answer.getArray())))