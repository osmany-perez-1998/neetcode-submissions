class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, min_idx = prices[0], 0
        profit = 0

        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
                min_idx = i
            else:
                profit = max(profit, prices[i] - min_val)
        
        return profit