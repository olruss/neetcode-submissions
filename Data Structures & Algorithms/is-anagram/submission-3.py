class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def d(word: str) -> dict[str, int]:
            res = {}
            for l in word:
                res[l] = res.get(l, 0) + 1
            return res
        return d(s) == d(t)