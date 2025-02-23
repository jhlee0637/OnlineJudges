#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10162                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10162                          #+#        #+#      #+#     #
#    Solved: 2025/02/23 12:14:02 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
T = int(sys.stdin.readline().strip())

time = [300, 60, 10] #A, B, C seconds
answer = list()
for tic in time:
    realNum = T//tic
    answer.append(realNum)
    T -= realNum*tic

if T!=0:
    print(-1)
else:
    print(*answer)
