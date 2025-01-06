#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1913                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: jhlee2020 <boj.kr/u/jhlee2020>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1913                           #+#        #+#      #+#     #
#    Solved: 2025/01/06 13:46:03 by jhlee2020     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
reading=sys.stdin.readlines()
n = int(reading[0].strip())
target = int(reading[1].strip())

m=3 #size of table: mxm
table = [[9, 2, 3],
         [8, 1, 4],
         [7, 6, 5]]

while n>m:
    m+=2 #increase oddly
    header = [m**2] + [table[0][0]+i for i in range(1,m)]
    tail = list(range(m**2-2*m+2, m**2-m+2))[::-1]
    leftGap = tail[0]+1 - table[-1][0]
    rightGap = header[-1]+1 - table[0][-1]

    #head
    new_table = [header]
    #mid
    for line in table:
        new_line = [line[0]+leftGap] + line + [line[-1]+rightGap]
        new_table.append(new_line)
    #tail
    new_table.append(tail)

    #assign
    table = new_table


for i in range(len(table)):
    print(*table[i])
    try:
        targetLoc = [i+1, table[i].index(target)+1]
    except:
        continue
print(*targetLoc)