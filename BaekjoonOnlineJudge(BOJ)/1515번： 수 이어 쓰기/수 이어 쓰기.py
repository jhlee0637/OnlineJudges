#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1515                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1515                           #+#        #+#      #+#     #
#    Solved: 2025/01/17 19:36:55 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
num=sys.stdin.readline()
num=num.strip()

answer=0
n=0
while True:
    n+=1
    if len(num)==0:
        break
    else:
        for s in str(n):
            if len(num)==0:
                break
            elif s==num[0]:
                answer=n
                num=num[1:]
print(answer)