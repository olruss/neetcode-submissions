class Solution:

    def _skip(self, l: str):
        return not (l.isalpha() or l.isdigit())
        
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if self._skip(s[l]):
                l += 1
                continue
            if self._skip(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True