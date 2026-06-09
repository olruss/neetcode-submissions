from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        res = -1
        steps = 0

        directions = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
        I, J = len(grid), len(grid[0])

        q = deque()
        q.append((0, 0))
        # seen = set()

        while q:
            steps += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                if (
                    i < 0 or j < 0
                    or i >= I or j >= J
                    or grid[i][j] == 1
                ):
                    continue
                grid[i][j] = 1  # danger -> mutation of the grid
                if (i, j) == (I - 1, J - 1):
                    return steps
                
                for di, dj in directions:
                    q.append((i + di, j + dj))

        return res