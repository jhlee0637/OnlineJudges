#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1015                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1015                           #+#        #+#      #+#     #
#    Solved: 2024/11/16 02:33:00 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
l = int(reading[0].strip())
nums = list(map(int, reading[1].strip().split(" ")))

stack=list()
answer=list()
for i_n in enumerate(nums):
    i, n = i_n
    sorted_i = sorted(nums).index(n)
    stack.append(n)
    finalIndex = sorted(nums).index(n)+stack.count(n)-1
    answer.append(finalIndex)
print(*answer)
