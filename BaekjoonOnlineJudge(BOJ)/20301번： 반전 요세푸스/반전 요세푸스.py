#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20301                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20301                          #+#        #+#      #+#     #
#    Solved: 2025/02/01 20:38:28 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

class ReJosephus():
    def __init__(self, N):
        self.q = deque(range(1, N+1)) # N>=1 #t:O(N) #s:O(N)

    def removeK(self, k, direction):
        if direction==True: #counter-clockwise 
            self.q.rotate(-(k-1)) #t: O(k-1)...O(N)
            remove = self.q.popleft() #remove #t: O(1)
        elif direction==False: #clockwise
            self.q.rotate(k-1) #t: O(k-1)...O(N)
            remove = self.q.pop() #remove #t: O(1)
        return remove

    def getQ(self):
        return self.q


N, K, M=list(map(int, sys.stdin.readline().strip().split(" ")))
array = ReJosephus(N)
cnt=0 #s:O(1)
direction=True #s:O(1)
while True:
    if len(array.getQ())==0:
        break
    else:
        remove = array.removeK(K, direction) #s:O(1)
        cnt+=1
        if cnt==M:
            direction = not direction #t: O(1)
            cnt=0
    print(remove)

#time complexity: O(NK)
'''
class를 이용한 deque 풀이
.rotate() 이용
'''
