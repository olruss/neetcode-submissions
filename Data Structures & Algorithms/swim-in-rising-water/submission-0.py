from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # brute force
        # for every time startin at 0 and growing incrementaly
        # try bfs as far as we can get
        # when decired node is reached - current time is an answer

        R, C = len(grid), len(grid[0])

        def bfs(t):
            q = deque()
            visited = set()
            q.append((0, 0))
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    if (
                        i < 0 or j < 0
                        or i >= R or j >= C
                        or (i, j) in visited
                        or grid[i][j] > t
                    ):
                        continue
                    if (i, j) == (R-1, C-1):
                        return True
                    visited.add((i, j))
                    

                    for di, dj in (
                        (1, 0), (0, 1), (-1, 0), (0, -1)
                    ):
                        q.append((i + di, j + dj))
            return False
                        


        i = 0
        while not bfs(i):
            i += 1
        
        return i
            

        