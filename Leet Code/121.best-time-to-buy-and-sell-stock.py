#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowPrice=prices[0]
        profit=0
        for todayPrice in prices[1:]:
            if todayPrice<lowPrice:
                lowPrice=todayPrice
            if todayPrice>lowPrice:
                potentialProfit=todayPrice-lowPrice
                if potentialProfit>profit:
                    profit=potentialProfit
        return profit
# @lc code=end

