#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1064                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1064                           #+#        #+#      #+#     #
#    Solved: 2024/12/28 15:46:11 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
x_a, y_a, x_b, y_b, x_c, y_c = map(float, sys.stdin.readline().strip().split(" "))

#lengths of the three lines
l_ab =((x_a-x_b)**2 + (y_a-y_b)**2)**(0.5)
l_bc =((x_b-x_c)**2 + (y_b-y_c)**2)**(0.5)
l_ac =((x_a-x_c)**2 + (y_a-y_c)**2)**(0.5)

#gradient of the three lines
try:
    g_ab = abs((y_b-y_a)/(x_b-x_a))
except:
    g_ab = 0
try:
    g_bc = abs((y_c-y_b)/(x_c-x_b))
except:
    g_bc = 0
try:
    g_ca = abs((y_c-y_a)/(x_c-x_a))
except:
    g_ca = 0

#if three gradients are equal -> can't make parallelogram
if g_ab == g_bc == g_ca:
    answer=-1.0
else:
    ls=list()
    ls.append(l_ab*2 + l_bc*2)
    ls.append(l_bc*2 + l_ac*2)
    ls.append(l_ab*2 + l_ac*2)
    answer=max(ls)-min(ls)

print(answer)