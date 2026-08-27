class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_idx =  0
        profit = 0

        for i in range(len(prices)):
            if prices[i] < prices[min_idx]:
                min_idx = i
            else:
                profit = max(profit, prices[i] - prices[min_idx])
        
        return profit