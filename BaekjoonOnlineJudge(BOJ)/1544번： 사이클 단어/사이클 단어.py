#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1544                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1544                           #+#        #+#      #+#     #
#    Solved: 2025/01/09 20:56:24 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()

wordBook = set()
for line in reading[1:]:
    line = line.strip()
    possibleWord = [line[i:]+line[:i] for i in range(len(line))]
    wordBook.add(min(possibleWord))
    
print(len(wordBook))