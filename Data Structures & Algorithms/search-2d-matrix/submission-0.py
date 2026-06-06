class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        l, r = 0, (rows * columns) - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = mid // columns, mid % columns
            v = matrix[row][col]
            if v == target:
                return True
            if v < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False