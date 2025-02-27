#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1010                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1010                           #+#        #+#      #+#     #
#    Solved: 2024/11/09 10:26:24 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()

import math
for line in reading[1:]:
    n, m = map(int, line.strip().split())
    combVal = math.comb(m, n)
    print(combVal)

"""
이 문제는 '조합'을 이용해서 해결해야 한다.
 - 서쪽의 site는 모두 연결되어야 한다.
 - 동쪽의 site는 모두 연결되지 않아도 괜찮다.
 - 따라서 동쪽의 site 중에서 무작위로 서쪽의 site 개수 만큼의 장소를 정하는 '조합'의 수를 계산한다.
 - 이후 그 조합의 수에서 서쪽으로 연결되는 다리의 경우의 수는 단 한가지일 것이다. 서로 겹칠 수 없기 때문이다.
"""