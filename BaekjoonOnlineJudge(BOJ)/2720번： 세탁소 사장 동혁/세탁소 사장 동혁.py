#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2720                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2720                           #+#        #+#      #+#     #
#    Solved: 2025/02/13 22:35:32 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading = sys.stdin.readlines()
T = reading[0]
for line in reading[1:]:
    C = int(line.strip())
    answer=list()
    QDNP = [25, 10, 5, 1]
    for coin in QDNP:
        answer.append(C//coin)
        C -= coin*(C//coin)
    print(*answer)
