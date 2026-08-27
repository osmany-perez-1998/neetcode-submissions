class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_balance = 0
        b_cool_balance = 0
        s_cool_balance = 0
        s_balance = prices[-1]

        for i in range(len(prices)-2, -1,-1):
            b_balance_1 = max(b_cool_balance,s_balance) - prices[i]
            b_cool_balance_1 = max(b_cool_balance,s_balance)
            s_cool_balance_1 = max(s_cool_balance, b_balance)
            s_balance = s_cool_balance + prices[i]

            b_balance,b_cool_balance,s_cool_balance = b_balance_1, b_cool_balance_1, s_cool_balance_1
        
        return max(b_balance,s_cool_balance)

        