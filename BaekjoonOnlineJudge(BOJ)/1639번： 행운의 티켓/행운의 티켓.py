#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1639                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1639                           #+#        #+#      #+#     #
#    Solved: 2025/01/08 16:46:55 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
num = [int(n) for n in input().strip()]

answer=0
for l in range(2,len(num)+1,2):
    for i in range(len(num)-l+1):
        left=num[i:i+l][:l//2]
        right=num[i:i+l][l//2:]
        if sum(left)==sum(right):
            answer=l
            break
print(answer)