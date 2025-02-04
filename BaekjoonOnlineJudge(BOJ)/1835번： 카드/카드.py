#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1835                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1835                           #+#        #+#      #+#     #
#    Solved: 2025/02/04 12:07:23 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
N = int(sys.stdin.readline())
revNum=list(reversed(range(1,N+1)))

answer=deque()
for n in revNum:
    answer.appendleft(n)
    while True:
        p = answer.pop()
        answer.appendleft(p)
        n-=1
        if n==0:
            break
        
print(*list(answer))