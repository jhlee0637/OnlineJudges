#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1051                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1051                           #+#        #+#      #+#     #
#    Solved: 2024/12/19 13:42:24 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
n, m = map(int, reading[0].strip().split(" "))
lines=[line.strip()for line in reading[1:]]

max=1
if n==1:
    pass
else:
    for i in range(n-1):
        for j in range(i+1, n):
            line= lines[i]
            nextLine=lines[j]
            gap=j-i
            for k in range(len(line)-gap):
                #AB
                #CD
                A=line[k]
                B=line[k+gap]
                C=nextLine[k]
                D=nextLine[k+gap]
                if A==B==C==D:
                    area = (gap+1)**2
                    if area>max:
                        max=area
print(max)
                