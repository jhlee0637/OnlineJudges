#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1057                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1057                           #+#        #+#      #+#     #
#    Solved: 2024/12/25 17:53:52 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
ppl, k, i = map(int, input().split(" "))
n = min(k, i)
m = max(k, i)

answer=-1
for i in range(ppl):
    if n-m!=0:
        if n%2==0:
            n=n//2
        else:
            n=(n//2)+1
        if m%2==0:
            m=m//2
        else:
            m=(m//2)+1
    elif n-m==0:
        answer=i
        break
    
print(answer)