#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2231                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2231                           #+#        #+#      #+#     #
#    Solved: 2024/11/22 14:37:15 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
n=sys.stdin.readline().strip()


# solution1. Brutal Force
n=int(n)
answer=0
for i in range(n+1):
    j=[int(tmp) for tmp in str(i)]
    m=sum(j)+i
    if m==n:
        answer="".join(map(str, j))
        break

print(answer)