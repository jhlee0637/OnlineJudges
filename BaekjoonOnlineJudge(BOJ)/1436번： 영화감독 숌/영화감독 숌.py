#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1436                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1436                           #+#        #+#      #+#     #
#    Solved: 2024/11/22 15:35:07 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
target = int(input())


# solution 1. Brutal Force
answer=False
cnt=0
n=0
while answer is False:
    n+=1
    if len(str(n).split("666"))>1:
        cnt+=1
    if cnt==target:
        answer=n
print(answer)