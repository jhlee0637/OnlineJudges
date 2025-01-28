#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2346                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2346                           #+#        #+#      #+#     #
#    Solved: 2025/01/28 22:07:46 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
class Ballon(): #dequeue
    def __init__(self, list):
        self.q = list
        self.i = 0
    
    def moveLeft(self):
        p = self.q.pop(0)
        self.q.append(p)
    
    def moveRight(self):
        p = self.q.pop(-1)
        self.q = [p] + self.q

    def getCard(self):
        if len(self.q)>0:
            card = self.q.pop(0)
            return card
        else:
            return False

    def getBallon(self):
        return self.q

import sys
reading=sys.stdin.readlines()
nums = list(map(int, reading[1].strip().split(" ")))

q = Ballon(nums)
i = Ballon(list(range(1, len(nums)+1)))
answer=list()
while True:
    card = q.getCard()
    answ = i.getCard()
    answer.append(answ)
    if len(q.getBallon())==0: #last card
        break
    else:
        if card>0:
            for c in range(card-1):
                q.moveLeft()
                i.moveLeft()
        elif card<0:
            for c in range(abs(card)):
                q.moveRight()
                i.moveRight()
print(*answer)

'''
class를 이용한 덱 구현
'''