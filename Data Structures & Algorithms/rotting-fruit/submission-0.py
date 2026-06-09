from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first iterate over whole matrix and find all rotten fruits
        # then for every rotten fruite run a bfs. one turn - one minute. all neighbours 1 -> 2 become rotten
        # repeat until there is nothing to rott
        # finally check the grid. if there are fresh fruits left -> -1 else -> number of turns
        
        q = deque()
        R, C = len(grid), len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        steps = 0
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        
        while q:
            has_fresh = False
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    _i, _j = i + di, j + dj
                    if (
                        _i < 0 or _j < 0
                        or _i >= R or _j >= C
                        or grid[_i][_j] != 1
                    ):
                        continue
                    else:
                        has_fresh = True
                        grid[_i][_j] = 2
                        q.append((_i, _j))
            if has_fresh:
                steps += 1
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return -1
        
        return steps





