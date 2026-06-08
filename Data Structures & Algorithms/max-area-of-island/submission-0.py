class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def dfs(i, j):
            if (
                i < 0 or j < 0
                or i >= len(grid) or j >= len(grid[0])
                or grid[i][j] != 1
            ):
                return 0
            grid[i][j] = 0  # mutation, be careful. function is not clean anymore

            cnt = 1
            for di, dj in directions:
                cnt += dfs(i + di, j + dj)
            
            return cnt

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area