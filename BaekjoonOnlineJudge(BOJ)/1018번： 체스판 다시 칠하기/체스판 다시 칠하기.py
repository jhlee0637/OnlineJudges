#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1018                           #+#        #+#      #+#     #
#    Solved: 2024/11/18 14:53:52 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
row, col = map(int, sys.stdin.readline().strip().split(" "))
lines = [reading.strip() for reading in sys.stdin.readlines()]

cnt=list()
for i in range(row-7):
    for j in range(col-7):
        bwFixCnt=0
        wbFixCnt=0
        for n in range(8):
            for m in range(8):

                sign=lines[i+n][j+m]
                if n%2==0 and m%2==0:
                    bwSign='B'
                    wbSign='W'
                elif n%2==0 and m%2!=0:
                    bwSign='W'
                    wbSign='B'
                elif n%2!=0 and m%2==0:
                    bwSign='W'
                    wbSign='B'
                elif n%2!=0 and m%2!=0:
                    bwSign='B'
                    wbSign='W'

                if sign!=bwSign:
                    bwFixCnt+=1
                if sign!=wbSign:
                    wbFixCnt+=1

        cnt.append(bwFixCnt)
        cnt.append(wbFixCnt)

print(min(cnt))

'''
다시 한번 브루탈포스로 풀어야 하는 문제
'''