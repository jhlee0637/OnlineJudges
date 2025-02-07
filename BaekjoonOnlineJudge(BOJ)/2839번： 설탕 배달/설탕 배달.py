#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2839                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2839                           #+#        #+#      #+#     #
#    Solved: 2025/02/07 16:52:41 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
N = int(sys.stdin.readline().strip())
answer=-1
if N%5==0:
    answer=N//5
else:
    maxBag=N//3
    for i in range(1,maxBag+1):
        small = i
        large = (N-(3*i))//5
        if small*3 + large*5 == N:
            answer = small + large
            break
print(answer)