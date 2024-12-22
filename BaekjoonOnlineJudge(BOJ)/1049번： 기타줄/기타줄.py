#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1049                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1049                           #+#        #+#      #+#     #
#    Solved: 2024/12/22 11:33:51 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
n, m = map(int, reading[0].strip().split())

packPrice=list()
singPrice=list()
for line in reading[1:]:
    line=line.strip().split(" ")
    packPrice.append(int(line[0]))
    singPrice.append(int(line[1]))
  
#case1. pack only
packNeed=n//6
if n%6 != 0:
    packNeed+=1
packOnlyPay= packNeed*min(packPrice)

#case2. pack + single
packNeed = n//6
singNeed = n%6
comboPay = packNeed*min(packPrice) + singNeed*min(singPrice)

#case3. single only
singPay = n * min(singPrice)

bestPay = min([packOnlyPay, comboPay, singPay])
print(bestPay)