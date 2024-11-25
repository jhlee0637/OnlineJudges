#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2563                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2563                           #+#        #+#      #+#     #
#    Solved: 2024/11/25 15:52:07 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
header = int(reading[0].strip())

######################################
# Solution1. Monte Carlo Integration #
######################################
# Create 100x100 xy array
xyArray = list()
for i in range(100):
    F_arry=[False]*100
    xyArray.append(F_arry)

# Marking all pointers of the array
cnt=0
for line in reading[1:]:
    x_1, y_1=map(int, line.strip().split(" "))

    # Find a pointer
    for i in range(x_1, x_1+10):
        for j in range(y_1, y_1+10):
            pointer = xyArray[i][j]

            # If the array is False > Mark it as True and count it
            if pointer is False:
                xyArray[i][j]=True
                cnt+=1

# Print the result
print(cnt)