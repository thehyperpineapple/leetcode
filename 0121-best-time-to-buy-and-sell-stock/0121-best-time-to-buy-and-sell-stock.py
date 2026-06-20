class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            sell = prices[i]
            if buy > sell:
                buy = prices[i]
            if sell - buy > profit:
                profit = sell - buy
        return profit
        