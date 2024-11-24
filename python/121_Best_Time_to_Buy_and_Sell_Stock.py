class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        profit=0
        for i in range(len(prices)):
            if prices[i]<buy:
                buy = prices[i]
            elif prices[i]-buy > profit:
                profit= prices[i]-buy   

        return profit
    
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
result = solution.maxProfit(prices)

print("Max profit:", result)    