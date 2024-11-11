#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1193                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1193                           #+#        #+#      #+#     #
#    Solved: 2024/11/12 02:26:22 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readline().strip()
idx = int(reading)

line=0
until=0
while idx>until:
    line+=1
    until+=line

gap = until-idx
if line%2 == 0:
    top = line-gap
    bottom = gap+1
else:
    top = gap+1
    bottom = line-gap

print(f'{top}/{bottom}')