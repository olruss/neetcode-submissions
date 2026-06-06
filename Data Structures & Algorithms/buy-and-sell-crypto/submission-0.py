class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers: buy & sell
        # on every itternation, move sell. update max profit.
        # if sell price is lower then buy -> move buy

        buy, sell = 0, 1
        profit = 0

        # [6, 7, 3, 5, 1] -> 2
        # [4] -> 0
        # [5, 3, 3] -> 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        
        return profit