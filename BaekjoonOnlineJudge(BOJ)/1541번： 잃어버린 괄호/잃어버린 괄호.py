#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1541                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1541                           #+#        #+#      #+#     #
#    Solved: 2025/02/17 20:01:22 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readline().strip()
sum=0
num=''
minusFlag=False
for i in range(len(reading)):
    s=reading[i]
    if s!="-" and s!="+":
        num+=reading[i]
    elif i==len(reading):
        num+=reading[i]

    if s=="-" or s=="+" or i==len(reading)-1:
        if minusFlag==True:
            sum-=int(num)
        elif s=="-":
            minusFlag=True
            sum+=int(num)
        else:
            sum+=int(num)
        num=''
print(sum)