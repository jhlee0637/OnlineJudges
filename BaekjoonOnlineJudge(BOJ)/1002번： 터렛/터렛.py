#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1002                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1002                           #+#        #+#      #+#     #
#    Solved: 2024/12/23 14:45:09 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
for line in reading[1:]:
    line=line.strip()
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, line.split())
    d = abs((x_1-x_2)**2 + (y_1-y_2)**2)**(0.5) #distance
    if d==0 and r_1==r_2: #contain
        answer=-1
    elif r_1+d<r_2 or r_2+d<r_1:
        answer=0
    elif r_1+d==r_2 or r_2+d==r_1: 
        answer=1
    else: #can not contain
        if r_1+r_2==d:
            answer=1
        elif r_1+r_2>d:
            answer=2
        elif r_1+r_2<d:
            answer=0
    print (answer)
    