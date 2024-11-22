#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2798                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2798                           #+#        #+#      #+#     #
#    Solved: 2024/11/22 11:47:04 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
n, m = map(int, reading[0].strip().split(" "))
nums = [n for n in map(int, reading[1].strip().split(" "))]

# solution1. Brutal Force
sums = list()
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i!=j and j!=k and i!=k:
                a = nums[i]
                b = nums[j]
                c = nums[k]
                if sum([a, b, c])<=m:
                    sums.append(sum([a, b, c]))

print(sorted(sums, reverse=True)[0])