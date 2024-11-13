#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1251                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1251                           #+#        #+#      #+#     #
#    Solved: 2024/11/13 12:21:45 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
seq = reading[0].strip()

seqs=list()
for i in range(len(seq)):
    for j in range(i+1,len(seq)):
        head=seq[:i][::-1]
        mid=seq[i:j][::-1]
        tail=seq[j:][::-1]
        s = head+mid+tail
        seqs.append(s)

print(sorted(seqs)[0])


'''
브루탈포스를 이용한 탐색은 시간복잡도가 n^2로 높기 때문에
그리디 알고리즘을 이용하여 시간복잡도를 낮춰보려고 고민했으나
한 시간 고민 끝에 쉽지 않다는 결론을 내렸다.

문제의 조건이 50글자 미만이었기 때문에 브루탈포스로도 가능했지만
만약 문자열의 길이가 길어진다면 비효율적인 풀이이다.
'''