#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2217                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2217                           #+#        #+#      #+#     #
#    Solved: 2025/02/14 15:28:14 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
N = int(reading[0].strip())
ropes = list(reversed([int(r.strip()) for r in reading[1:]]))

maxW = 0
for k  in range(N):
    w = min(ropes[:k+1])*(k+1)
    if maxW>w:
        break
    else:
        maxW = w
    

print(maxW)