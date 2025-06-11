
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit=0
        for buy_price,sell_price in pairwise(prices):
            profit=max(0,sell_price - buy_price)
            total_profit += profit
        
        return total_profit