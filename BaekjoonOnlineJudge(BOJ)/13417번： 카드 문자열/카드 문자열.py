#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13417                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13417                          #+#        #+#      #+#     #
#    Solved: 2025/01/24 17:00:12 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# Deque practice 2
import sys

class Deque:
    def __init__ (self):
        self.q = list()

    def addFront(self, X):
        self.q = [X] + self.q
        return self.q
    
    def addBack(self, X):
        self.q.append(X)
        return self.q
    
    def popFront(self): #skip the empty case
        pop = self.q[0]
        self.q.pop(0)
        return pop
    
    def getAll(self):
        return self.q

T=int(sys.stdin.readline())
reading=sys.stdin.readlines()
for i in range(T):
    line=reading[i*2+1].strip().split(" ")
    adv = Deque()
    adv.addFront(line[0])
    for s in line[1:]:
        card=adv.popFront()
        frontAdded=s+card
        backAdded=card+s
        adv.addFront(sorted([frontAdded, backAdded])[0])
        adv.addBack(sorted([frontAdded, backAdded])[1])
    print(adv.getAll()[0])


'''
클래스 연습 및 큐 알고리즘 이해를 도모
'''