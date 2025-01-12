#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1059                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1059                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 19:31:56 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading = sys.stdin.readlines()
L = int(reading[0].strip())
S = list(map(int, reading[1].strip().split(" ")))
n = int(reading[2].strip())

if n in S:
    answer=0
    
else:
    S.append(n)
    S.sort()
    i = S.index(n)

    if i==0:
        left = range(1, n)
        right = range(n+1, S[1])
        endToend = len(left)*len(right)

    elif i==len(S)-1:
        left = range(S[-2]+1, n)
        right = range(n+1, 1001)
        endToend = len(left)*len(right)

    else:
        left = range(S[i-1]+1, n)
        right = range(n+1, S[i+1])
        endToend = len(left)*len(right)

    answer=len(left)+len(right)+endToend

print(answer)