class Solution:
    def climbStairs(self, n: int) -> int:
        # dfs with memoisation
        # starting from n we will create two brunches: 1, 2 steps
        # base case: n = 0 -> return 1 (we found one path)
        # if n < 0 -> return 0 (missed the target)
        # check memo when enter dfs, update before exit

        memo = {}

        # 0 1 2 3
        #    3
        #  2    1
        # 1  0 0  -1
        # 0 
        
        def dfs(stair):
            if stair < 0:
                return 0
            if stair in memo:
                return memo[stair]
            if stair == 0:
                return 1
            
            res = dfs(stair - 1) + dfs(stair - 2)
            memo[stair] = res
            return res
        
        return dfs(n)
            