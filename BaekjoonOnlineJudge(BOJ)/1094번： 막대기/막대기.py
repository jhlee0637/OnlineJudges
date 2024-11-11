#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1094                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1094                           #+#        #+#      #+#     #
#    Solved: 2024/11/11 09:34:53 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import combinations

target = int(sys.stdin.readline().strip())
s = 64

# 1. 약수 구하기
nums=list()
for n in range(1, s+1):
    if s%n == 0:
        nums.append(n)

# 2. `combinations`을 이용하여 조합의 합을 구하기
count=0
while count<len(nums):
    count+=1
    combos=list(combinations(nums, count))
    for c in combos:
        if sum(c)==target:
            print(count)