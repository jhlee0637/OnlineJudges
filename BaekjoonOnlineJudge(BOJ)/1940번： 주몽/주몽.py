#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1940                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1940                           #+#        #+#      #+#     #
#    Solved: 2025/01/15 22:40:36 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading = sys.stdin.readlines()
N = int(reading[0].strip())
M = int(reading[1].strip())
nums = sorted(map(int, reading[2].strip().split()))

left = 0
right = N - 1
answer = 0

while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == M:
        answer += 1
        left += 1
        right -= 1
    elif current_sum < M:
        left += 1
    else:
        right -= 1

print(answer)
