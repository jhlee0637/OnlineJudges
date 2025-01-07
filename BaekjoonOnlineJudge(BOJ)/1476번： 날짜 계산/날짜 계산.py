#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1476                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1476                           #+#        #+#      #+#     #
#    Solved: 2025/01/07 20:56:23 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
tarE, tarS, tarM = map(int, sys.stdin.readline().strip().split(" "))

n=1
e=1
s=1
m=1

answer=0
while n<8000:
    if e==tarE and s==tarS and m==tarM:
        break
    else:
        n+=1
        e+=1
        s+=1
        m+=1
        if e==16:
            e=1
        if s==29:
            s=1
        if m==20:
            m=1
print(n)