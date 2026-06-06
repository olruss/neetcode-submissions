class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        if not s1:
            return True

        s1a = [0] * 26
        idx = lambda c: ord(c) - ord('a')

        for l in s1:
            s1a[idx(l)] += 1
        
        l, r = 0, len(s1) - 1
        s2a = [0] * 26
        def _add(c):
            s2a[idx(c)] += 1
        
        def _rm(c):
            s2a[idx(c)] -= 1

        l = 0
        for r, c in enumerate(s2):
            _add(c)
            window = r - l + 1

            if window > len(s1):
                _rm(s2[l])
                l += 1
            if s1a == s2a:
                return True
        return False
            