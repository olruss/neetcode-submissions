class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top-down
        # DFS
        # as we coins are not limited,
        # for every step we are able to include every of the coin
        # so we will iterate over all coints
        # and run dfs(amount - coin_value)
        # base case - amoun < 0 -> return 0
        # amount == 0 -> 1
        #
        # we can memorize the remaining amount: min number of coins

        memo = {}
        if amount == 0:
            return 0

        def dfs(remaining):
            if remaining < 0:
                return float('inf')
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            res = 1 + min(dfs(remaining - c) for c in coins)
            memo[remaining] = res
            return res
        
        res = dfs(amount)
        return -1 if res == float('inf') else res
