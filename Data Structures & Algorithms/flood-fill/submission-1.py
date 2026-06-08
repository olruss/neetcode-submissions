class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(i, j, c):
            if (
                i < 0 or j < 0
                or i >= len(image) or j >= len(image[0])
                or image[i][j] == color
                or image[i][j] != c
            ):
                return
            
            image[i][j] = color

            for di, dj in (
                (1, 0), (-1, 0), (0, 1), (0, -1)
            ):
                dfs(i + di, j + dj, c)
            
        dfs(sr, sc, image[sr][sc])
        return image