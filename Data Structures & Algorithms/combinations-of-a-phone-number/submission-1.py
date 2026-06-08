class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # backtracking

        if not digits:
            return []

        d2l = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        cur = []

        def bt(i):
            if i >= len(digits):
                res.append(cur.copy())
                return
            
            for l in d2l[digits[i]]:
                cur.append(l)
                bt(i + 1)
                cur.pop()
        
        bt(0)

        return ["".join(r) for r in res]