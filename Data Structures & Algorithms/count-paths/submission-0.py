class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dfs + memo
        # as we going in two directions towards the finish
        # there is no chance of going in circle
        # that's important, no need to track visited cells when going deep
        # than for every tree node we'll have two decitions: down or right
        # when we go out of grid - return 0
        # when we hit the target - that's 1
        # use memo

        # time is O(N), space is O(N)

        memo = {(m-1, n-1): 1}
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = dfs(i + 1, j) + dfs(i, j + 1)
            memo[(i, j)] = res

            return res
        
        return dfs(0, 0)
            