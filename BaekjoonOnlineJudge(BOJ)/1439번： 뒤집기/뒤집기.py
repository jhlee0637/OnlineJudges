#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1439                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1439                           #+#        #+#      #+#     #
#    Solved: 2025/02/20 00:36:36 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
nums=sys.stdin.readline().strip()
zero_one=0
one_zero=0

for i in range(len(nums)):
    if i==0:
        if nums[i]=='0':
            one_zero+=1
        else:
            zero_one+=1
    elif nums[i-1]=='0' and nums[i]=='1':
        zero_one+=1
    elif nums[i-1]=='1' and nums[i]=='0':
        one_zero+=1

answer=min(zero_one, one_zero)
print(answer)