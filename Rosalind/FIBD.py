'''
https://rosalind.info/problems/fibd/

Problem:: Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”,
          which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month
          and produces a single pair of offspring (one male, one female) each subsequent month.

          Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months.
          
          See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset: 6 3

Sample Output:  4
'''

def makeMemo(monthUntil, monthLive):
    memo=[1,1]
    for i in range(2, monthUntil):
        if i<monthLive: #before death start
            death=0
        if i>=monthLive and i-monthLive-1>=0 : #after death start
            death=memo[i-monthLive-1]
        elif i>=monthLive and i-monthLive-1<0: #First death
            death=1
        val=memo[i-1]+memo[i-2]-death
        print(f'i={i} val={memo[i-1]}+{memo[i-2]}-{death}={val}')
        memo.append(val)
    return memo
    
if __name__=="__main__":
    monthUntil=6
    monthLive=3
    print(makeMemo(monthUntil, monthLive))