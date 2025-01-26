#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3190                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3190                           #+#        #+#      #+#     #
#    Solved: 2025/01/26 21:23:31 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
class Deque:
    def __init__(self):
        self.q=[[0,0]]
        self.dirIdx=0 
        self.dir=[[0,1], [-1,0], [0, -1], [1,0]] #positive y direction first

    def getHead(self):
        return self.q[0]
    
    def getTail(self):
        return self.q[-1]
    
    def getAll(self):
        return self.q
    
    def getDir(self):
        idx = int(self.dirIdx)%4
        dir = self.dir[idx]
        return dir

    def moveHead(self, appleLoc, N):
        tmpHead = [prev+next for prev, next in zip(self.getHead(), self.getDir())]
        if tmpHead in self.getAll(): #crush to body
            self.q=[tmpHead]+self.q
            return False       
        elif tmpHead in appleLoc: #eat apple, not moving tail
            self.q=[tmpHead]+self.q
            appleLoc.remove(tmpHead) #remove apple 
        elif tmpHead[0]>=N or tmpHead[1]>=N or tmpHead[0]<0 or tmpHead[1]<0: #crush to the wall
            self.q=[tmpHead]+self.q
            return False    
        else: #move to empty place
            self.q.pop(-1)
            self.q=[tmpHead]+self.q

    def turnHead(self, cmd):
        if cmd == "L":
            self.dirIdx+=1
        elif cmd == "D":
            self.dirIdx-=1

import sys
reading=sys.stdin.readlines()
N = int(reading[0].strip())
K = int(reading[1].strip())

appleLoc=list()
for i in range(2, 2+K):
    m, n = reading[i].strip().split(" ")
    m = int(m) - 1 #zero base
    n = int(n) - 1 #zero base
    appleLoc.append([m, n])

turnCmds=dict() #[time:turn direction]
for i in range(2+K+1, len(reading)):
    X, C = reading[i].strip().split(" ")
    turnCmds[int(X)]=C #C: L=left, D=right

snake = Deque()
time=0
#print(time, snake.getAll())
while True:
    cmd = turnCmds.get(time, False)
    if cmd != False:
        snake.turnHead(cmd)
    time+=1
    if snake.moveHead(appleLoc, N) !=False:
        #print(time, snake.getAll())
        pass
    else:
        #print(time, "---DEAD---", snake.getAll())
        break
print(time)    

'''
Class를 이용한 큐 구현 연습
'''