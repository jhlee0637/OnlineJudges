#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1448                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1448                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 17:15:04 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
nums = sorted(list(int(line.strip()) for line in reading[1:]), reverse=True)

answer=-1
for i in range(len(nums)-2):
    if answer==-1:
        for j in range(i+1,len(nums)-1):
            if answer==-1:
                for k in range(j+1, len(nums)):
                    A=nums[i]
                    B=nums[j]
                    C=nums[k]
                    if A<B+C:
                        answer=A+B+C
                        break
                    elif A>=B+C:
                        break
            else:
                break
    else:
        break
print(answer)