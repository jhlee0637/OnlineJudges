'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
    - Input: prices = [7,1,5,3,6,4]
    - Output: 7
    - Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
                Total profit is 4 + 3 = 7.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices)==1:
            return 0
            exit

        totalProfit=0
        wallet=prices[0]
        prices.append(0)
        for i in range(1, len(prices)):
            yesterPrice=prices[i-1]
            todayPrice=prices[i]
            
            if i==len(prices)-1:
                pass
            else:
                tomorrowPrice=prices[i+1]

            if (yesterPrice-todayPrice)>=0 and (todayPrice-tomorrowPrice)<0:
                #buy!
                wallet=todayPrice
                print(todayPrice, "BUY", "wallet:", wallet)
            elif (yesterPrice-todayPrice)<0 and (todayPrice-tomorrowPrice)>=0:
                #sell!
                todayProfit=todayPrice-wallet
                totalProfit+=todayProfit
                wallet=0
                print(todayPrice, "SELL",  "wallet:", wallet, "totalProfit", totalProfit)
            else:
                #hold!
                continue


        return totalProfit