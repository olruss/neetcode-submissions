class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "canada", 2 -> 5

        max_count = 0
        seen = {}
        l, r = 0, 0
        res = 0

        while r < len(s):
            seen[s[r]] = seen.get(s[r], 0) + 1
            max_count = max(max_count, seen[s[r]])

            while r - l - max_count + 1 > k:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            
            r += 1
        
        return res