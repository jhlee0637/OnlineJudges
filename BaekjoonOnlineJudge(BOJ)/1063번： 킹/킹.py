#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1063                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1063                           #+#        #+#      #+#     #
#    Solved: 2024/12/24 14:58:06 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
king, rock, n = reading[0].strip().split(" ")

X=[chr(i) for i in range(65, 73)]
Y=[str(i) for i in range(1, 9)]

king_xi=X.index(king[0])
king_yi=Y.index(king[1])
rock_xi=X.index(rock[0])
rock_yi=Y.index(rock[1])

orders={"R":[1,0],
        "L":[-1,0],
        "B":[0,-1],
        "T":[0,1],
        "RT":[1,1],
        "LT":[-1,1],
        "RB":[1,-1],
        "LB":[-1,-1]}

for line in reading[1:]:
    order=orders[line.strip()]
    next_xi=king_xi + order[0]
    next_yi=king_yi + order[1]
    next_rock_xi=rock_xi
    next_rock_yi=rock_yi
    if next_xi<0 or next_xi>7 or next_yi<0 or next_yi>7: #king will be out
        next_xi=king_xi
        next_yi=king_yi
    else: #king won't be out
        if next_xi==rock_xi and next_yi==rock_yi: #rock push consider
            next_rock_xi = rock_xi + order[0]
            next_rock_yi = rock_yi + order[1]
            if next_rock_xi<0 or next_rock_xi>7 or next_rock_yi<0 or next_rock_yi>7: #rock will be out
                next_rock_xi=rock_xi
                next_rock_yi=rock_yi
                next_xi=king_xi
                next_yi=king_yi
            else: #rock push confirm
                pass
        else: #rock won't be touched
            pass

    #print(f'{X[king_xi]}{Y[king_yi]} -> {X[next_xi]}{Y[next_yi]} | {X[rock_xi]}{Y[rock_yi]} -> {X[next_rock_xi]}{Y[next_rock_yi]}')
    king_xi=next_xi
    king_yi=next_yi
    rock_xi=next_rock_xi
    rock_yi=next_rock_yi
    
print(f'{X[next_xi]}{Y[next_yi]}')
print(f'{X[next_rock_xi]}{Y[next_rock_yi]}')