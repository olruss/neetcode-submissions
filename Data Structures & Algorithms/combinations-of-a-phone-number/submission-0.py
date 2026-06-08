from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        q = deque()
        for d in digits:
            if not q:
                for l in d2l[d]:
                    q.append(l)
                continue
            for _ in range(len(q)):
                comb = q.popleft()
                for l in d2l[d]:
                    q.append(comb + l)
        return list(q)