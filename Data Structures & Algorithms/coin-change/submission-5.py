class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # lets try bottom-up DP
        # say we have coins 3 4 1 that should result to 7
        # we will create array [0...amount]
        # initially it will be instantiated with float('inf) for
        # members 1..amount (by default assume you can't reach the goal)
        #
        # then we will iterate over coins
        # and then try it for every given amount
        # we will check, can we do better then previous round
        # if we can - update, if not - keep previous value
        # 
        # how would we calculate the number of coins:
        # amount // coin + memo[amount % coin]
        #
        # complexity - time N*Amount
        # space O(N)

        memo = [float('inf')] * (amount + 1)
        memo[0] = 0

        for c in coins:
            for target, cnt in enumerate(memo):
                if target - c >= 0:
                    memo[target] = min(cnt, 1 + memo[target-c])
        
        return -1 if memo[-1] == float('inf') else memo[-1]
