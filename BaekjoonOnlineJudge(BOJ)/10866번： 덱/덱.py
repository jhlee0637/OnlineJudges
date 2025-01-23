#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10866                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10866                          #+#        #+#      #+#     #
#    Solved: 2025/01/23 19:10:05 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
class Deque:
    def __init__(self):
        self.q = list()

    def push_front(self, X):
        self.q = [X] + self.q
  
    def push_back(self, X):
        self.q = self.q + [X]
        
    def pop_front(self):
        if len(self.q)==0:
            return -1
        else:
            front = self.q[0]
            self.q.pop(0)
            return front
        
    def pop_back(self):
        if len(self.q)==0:
            return -1
        else:
            back = self.q[-1]
            self.q.pop(-1)
            return back
        
    def size(self):
        if len(self.q)==0:
            return 0
        else:
            return len(self.q)
    
    def empty(self):
        if len(self.q)==0:
            return 1
        else:
            return 0
        
    def front(self):
        if len(self.q)==0:
            return -1
        else:
            return self.q[0]
        
    def back(self):
        if len(self.q)==0:
            return -1
        else:
            return self.q[-1]

import sys
reading=sys.stdin.readlines()

deck = Deque()
for line in reading[1:]:
    command=line.strip().split(" ")
    if len(command)==1:
        answer=getattr(deck, command[0])()
    elif len(command)==2:
        answer=getattr(deck, command[0])(int(command[1]))
    
    if answer is not None:
        print(answer)