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
ropes = [int(r.strip()) for r in reading[1:]]
ropes.sort(reverse=True)

weights = list()
for k  in range(N):
    w = ropes[k]*(k+1)
    weights.append(w)
    
print(max(weights))