import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra
        # use max level on a path for sorting
        # so we will push
        # (max-on-path, i, j)

        R, C = len(grid), len(grid[0])

        h = [(grid[0][0], 0, 0)]
        visited = set()

        while h:
            t, i, j = heapq.heappop(h)
            if (i, j) == (R - 1, C - 1):
                return t
            if (i, j) in visited:
                continue
            visited.add((i, j))

            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                _i, _j = i + di, j + dj
                if (
                    _i < 0 or _j < 0
                    or _i >= R or _j >= C
                ):
                    continue
                heapq.heappush(h, (max(t, grid[_i][_j]), _i, _j))
        