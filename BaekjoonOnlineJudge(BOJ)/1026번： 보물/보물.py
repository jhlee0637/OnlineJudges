#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1026                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1026                           #+#        #+#      #+#     #
#    Solved: 2024/12/18 14:13:26 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines() #O(M, length of reading)
nums1=sorted([int(n) for n in reading[1].strip().split(" ")]) #sorted = O(NlogN, Timsort)
nums2=sorted([int(n) for n in reading[2].strip().split(" ")], reverse=True) #sorted = O(NlogN, Timsort)

sum=0
for i in range(len(nums1)): #O(N)
    sum+=nums1[i]*nums2[i]
print(sum) #Total time complexity: O(M) + 2*O(NlogN) + O(N) ≈ O(NlogN)