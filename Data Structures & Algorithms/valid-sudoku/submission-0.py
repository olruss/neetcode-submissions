class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for c in range(9):
            for r in range(9):
                col = cols[c % 9]
                row = rows[r % 9]
                box = boxes[c // 3][r // 3]

                val = board [c][r]
                if not val or val == ".":
                    continue
                if val in col or val in row or val in box:
                    return False
                col.add(val)
                row.add(val)
                box.add(val)
        
        return True

                