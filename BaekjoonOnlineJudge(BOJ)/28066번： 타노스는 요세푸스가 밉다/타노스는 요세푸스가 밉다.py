#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28066                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28066                          #+#        #+#      #+#     #
#    Solved: 2025/02/05 19:44:02 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
N, K = list(map(int, sys.stdin.readline().strip().split(" ")))
answer=False

squ = deque(range(1,N+1)) #generate deque #t: O(N)
while True:
    if len(squ)<K: #option #len(squ) = t: O(1)
        answer=squ.popleft()
        break
    else:
        squ.rotate(-1) #t: O(K)
        for n in range(K-1): #t: O(K)
            squ.popleft()
        squ.rotate(1) #t: O(K)

    if len(squ)>=2:
        squ.rotate(-1)
print(answer)

#time complexity: O(N*K)