#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11047                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11047                          #+#        #+#      #+#     #
#    Solved: 2024/11/23 14:19:09 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading = sys.stdin.readlines() #read input
n, k = map(int, reading[0].strip().split(" ")) #header. n: types of coins. k: sum value target
vals = sorted([int(n.strip()) for n in reading[1:]], reverse=True) #values of each coins, sort in descending order

# solution1. greedy algorithm
cnt=0
target=k
li_cnt=list()
answer=False
for i in range(len(vals)):
    val = vals[i]
    tmp_cnt = target//val
    #print(cnt, val, target)
    if tmp_cnt>0:
        target=target-(target//val)*val
        cnt+=tmp_cnt
    if target==0: #nothing left
        answer=cnt
    li_cnt.append(tmp_cnt)


# answer validation
validationValue=0
for i in range(len(li_cnt)):
    validationValue+=li_cnt[i]*vals[i]    
# Error test
if answer==False:
    print("Error: answer is not defined")
elif target>0:
    print(f"Error: target is remain: {target}")
elif validationValue!=k:
    print(f"Error: sum is not matched. validationValue:{validationValue}<->k:{k}")
else: #Correct
    print(answer)