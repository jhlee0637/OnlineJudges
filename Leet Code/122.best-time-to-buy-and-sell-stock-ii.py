#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
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
        
# @lc code=end

