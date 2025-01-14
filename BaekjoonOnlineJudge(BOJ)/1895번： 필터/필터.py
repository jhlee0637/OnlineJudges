#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1895                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1895                           #+#        #+#      #+#     #
#    Solved: 2025/01/14 20:43:22 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()

R, C = list(map(int, reading[0].strip().split(" ")))
T = int(reading[-1].strip())


table=list()
for line in reading[1:-1]:
    line=list(map(int, line.strip().split(" ")))
    table.append(line)

answer=0
for r in range(R-2):
    for c in range(C-2):
        nums=list()
        nums+=table[r][c:c+3]
        nums+=table[r+1][c:c+3]
        nums+=table[r+2][c:c+3]

        mid=sorted(nums)[4]
        if mid>=T:
            answer+=1

print(answer)