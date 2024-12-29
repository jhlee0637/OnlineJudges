#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1004                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1004                           #+#        #+#      #+#     #
#    Solved: 2024/12/29 13:50:58 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
T = int(reading[0].strip())

for i in range(1, len(reading)):
    line=list(map(int, reading[i].strip().split(" ")))
    if len(line)==4:
        x_1, y_1, x_2, y_2 = list(map(int, reading[i].strip().split(" ")))
        planetCnt=int(reading[i+1].strip())
        
        planetXYR = list()
        for l in reading[i+2:i+2+planetCnt]:
            planetXYR.append(list(map(int, l.strip().split(" "))))
        
        answer=0
        for XYR in planetXYR:
            X, Y, R = XYR
            #distance from start to XY
            disStrt = ((Y-y_1)**2+(X-x_1)**2)**(0.5)
            #distance from destination to XY
            disDest = ((Y-y_2)**2+(X-x_2)**2)**(0.5)
            if disStrt>R and disDest>R: #out of circle
                pass
            elif disStrt<R and disDest<R: #can't leave circle
                pass
            else: #One of them is in cirlce and rest of them is out of circle
                answer+=1
        print(answer)

'''
시작점을 포함하는 원의 개수 + 도착점을 포함하는 원의 개수
'''