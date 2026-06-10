class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP bottom up
        # as we moving in two directions,
        # for every given cell, 
        # number of ways to get there is
        # is a sum of number of ways to get to the cell above and to the left
        # so asume we have 2x2 grid
        # we'll count starting from (0, 0)
        # 1 -  ->  1 1   ->   1 1    ->    1 1 
        # - -      - -        1 -          1 2

        # we can have matrix to store that
        # but as we access only row above and value on the right,
        # we can optimize by just having two rows (prev row and current)
        # or
        # we can do even better and create a single array with lengh of n + 1 
        # with 0 item alway 0 (cuz value on the left always 0)
        # and rest of items is 1 (for first row, all cells will have only 1 way)
        # it will represent the first row
        # and then just update value above as we moving forward
        # so value from the left will be actually current index - 1 of that array


        memo = [1] * (n + 1)
        memo[0] = 0


        for i in range(1, m):
            for j in range(n):
                memo[j + 1] = memo[j + 1] + memo[j]
        
        return memo[-1]

        # let's trace this with our example m = 2, n = 2
        # memo (row 1) = [0, 1, 1]
        # 1 outer cycle, 2 inner cycles
        # [0, 1, 1] -> [0, 1, 1] -> [0, 1, 2]

