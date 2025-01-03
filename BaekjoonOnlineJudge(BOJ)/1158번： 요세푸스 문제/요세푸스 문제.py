#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1158                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1158                           #+#        #+#      #+#     #
#    Solved: 2025/01/03 19:42:51 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, k = map(int, input().strip().split())
nums = list(range(1, n+1))
k = k-1

answer = []
while nums:
    idx = k % len(nums)
    answer.append(str(nums.pop(idx)))
    nums = nums[idx:] + nums[:idx]

print(f'<{", ".join(answer)}>')