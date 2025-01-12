#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4375                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4375                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 18:17:02 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input=sys.stdin.readlines()
nums = [int(x) for x in input]
rests = [0 for i in range(len(nums))]
answers = [0 for i in range(len(nums))]

cnt=0
oneX=0
while answers.count(0)>0:
    tenX = 10**cnt
    oneX += tenX
    for j in range(len(nums)):
        rest = rests[j]
        divide = nums[j]
        answer = answers[j]
        
        rest += tenX%divide
        rests[j]=rest
        if rest%divide==0 and answer==0:
            answers[j]=len(str(oneX))
    cnt+=1


for answer in answers:
    print(answer)

'''
필요 이상으로 수학적으로 접근했다.
간단한 풀이로는 str(1)을 계속 붙여가면서 나머지가 0이 되는지 확인하는 방법이 있다.
'''