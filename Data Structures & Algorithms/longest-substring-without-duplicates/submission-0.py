class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a sliding window (two pointers)
        # store seen charecters in a set
        # initially both pointers are on 0
        # on every itteration check char under right pointer
        # if it's not seen -> update max_substring (r - l + 1)
        #       and more r right
        # if seen -> pop charecter under right pointer from seen and move right until left char in seen

        seen = set()
        l, r = 0, 0
        res = 0
        # "xyzza" -> 3
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            seen.add(s[r])
            r += 1
        
        return res