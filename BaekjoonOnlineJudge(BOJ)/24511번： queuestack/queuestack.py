#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24511                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24511                          #+#        #+#      #+#     #
#    Solved: 2025/02/02 17:39:31 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
reading=sys.stdin.readlines()
N = int(reading[0].strip())
A = list(map(int, reading[1].strip().split(" ")))
B = list(map(int, reading[2].strip().split(" ")))
M = int(reading[3].strip())
C = list(map(int, reading[4].strip().split(" ")))

answer=deque()
for i in range(N):
    if A[i]==0:
        answer.appendleft(B[i])

if len(answer)>=M:
    answer=list(answer)[:M]
else:
    for i in range(M-len(answer)):
        answer.append(C[i])

print(*answer)