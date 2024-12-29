#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1021                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1021                           #+#        #+#      #+#     #
#    Solved: 2024/12/30 06:35:11 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading = sys.stdin.readlines()
n, m = list(map(int, reading[0].strip().split(" ")))
targets = list(map(int, reading[1].strip().split(" ")))

q = list(range(1, n+1))
totalCost=0
for t in targets:
    targetIdx = q.index(t)
    if targetIdx==0:
        q=q[1:]
    else:
        cost_2 = targetIdx
        cost_3 = len(q)-targetIdx
        q=q[targetIdx+1:]+q[:targetIdx]
        totalCost+=min([cost_2, cost_3])
print(totalCost)