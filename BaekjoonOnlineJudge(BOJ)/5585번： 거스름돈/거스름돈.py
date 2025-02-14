#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5585                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5585                           #+#        #+#      #+#     #
#    Solved: 2025/02/14 15:24:35 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
price = int(sys.stdin.readline())
coins = [500, 100, 50, 10, 5, 1]

change = 1000-price
answer = 0
for c in coins:
    answer += change//c
    change -= c*(change//c)

print(answer)