#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1812                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1812                           #+#        #+#      #+#     #
#    Solved: 2025/01/10 09:14:15 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
n = int(reading[0])
answer=list()

m=0
for i in range(1,n+1):
    if i%2==0:
        m -= int(reading[i])
    else:
        m += int(reading[i])
answer.append(m//2)

for i in range(1, n):
    gap = int(reading[i])
    answer.append(gap-answer[-1])

for a in answer:
    print(a)