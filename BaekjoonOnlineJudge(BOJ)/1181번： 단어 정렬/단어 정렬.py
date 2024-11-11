#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1181                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1181                           #+#        #+#      #+#     #
#    Solved: 2024/11/12 02:01:44 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
lenWords=dict()
for s in sys.stdin.readlines()[1:]:
    s = s.strip()
    n = len(s)
    lenWords[n] = lenWords.get(n, list())
    if lenWords[n].count(s)==0:
        lenWords[n].append(s)

for d in sorted(lenWords.items(), key=lambda X:X[0]):
    n, words = d
    for s in sorted(words):
        print(s)