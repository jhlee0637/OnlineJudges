#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for n in range(len(ratings))] #every students have at least one candy #s: O(n)
        for i in range(1, len(ratings)): #search from left to right #t: O(n)
            prevRate = ratings[i-1]
            rate = ratings[i]
            if prevRate<rate and candies[i-1]>=candies[i]: #if the present rate is higher but the candy is lower
                candies[i]=candies[i-1]+1 #replace the candy to the amount one candy more than the previous rate

        ratings=ratings[::-1] #to search from right to left, change the array direction #t: O(n) s:O(n)
        candies=candies[::-1] #t: O(n) s:O(n)
        for i in range(1, len(ratings)): #repeat #t: O(n)
            prevRate = ratings[i-1]
            rate = ratings[i]
            if prevRate<rate and candies[i-1]>=candies[i]:
                candies[i]=candies[i-1]+1

        answer=sum(candies)
        return answer
    
#Time complexity: O(n)
#Space complexity: O(n)

# @lc code=end

