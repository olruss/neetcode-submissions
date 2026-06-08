class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        directions = (
            (1, 0), (0, 1), (-1, 0), (0, -1)
        )

        # if allowed to mutate the initial grid,
        # I'll mark the visited nodes.
        # othervise I can use set of coordinates (tuples)
        visited = "X"

        def dfs(i, j):
            if (
                i < 0 or j < 0
                or i >= len(grid) or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return
            grid[i][j] = visited

            for di, dj in directions:
                dfs(i + di, j + dj)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        
        return cnt