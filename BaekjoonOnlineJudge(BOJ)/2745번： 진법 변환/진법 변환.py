#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2745                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2745                           #+#        #+#      #+#     #
#    Solved: 2024/12/01 14:26:40 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
n, b = reading[0].strip().split(" ")
n=str(n)
b=int(b)

# Solution 1. Python
'''
answer = int(n, b)
'''

# Solution 2. Manual method
# Map characters to their values
chaVal={chr(65+i):10+i for i in range(26)}
for i in range(10):
    chaVal[str(i)]=i

# Initialize the result
answer=0

# Process each characters
for i in range(len(n)):
    cha=n[i]
    val=chaVal[cha]

    # Calculate the exponent
    if len(n)>0:
        exp=len(n)-i-1
    elif len(n)==1:
        exp=0

    # Calculate the value
    answer+=val*(b**exp)


# Answer
print(answer)
