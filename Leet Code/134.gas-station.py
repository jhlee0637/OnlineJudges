#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        answer=-1
        if sum(gas)<sum(cost):
            pass
        else:
            left_gas=0
            for i in range(len(gas)):
                left_gas += gas[i]-cost[i]
                if left_gas>=0 and answer==-1:
                    answer=i
                elif left_gas<0:
                    answer=-1
                    left_gas=0
        return answer


'''
1.  gas의 총합은 cost의 총합보다 항상 커야 한다.
    이를 만족한다면, solution은 항상 존재할 수 밖에 없다.

2.  "If there exists a solution, it is guaranteed to be unique."
    모든 gas station마다 경우의 수를 계산해야할 필요가 없다.
    한 station이라도 시작조건을 만족한다면 거기를 시작점으로 잡는다
'''
# @lc code=end

