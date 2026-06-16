class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}

        s = 0
        res = 0
        for n in nums:
            s += n
            if s-k in seen:
                res += seen[s-k]
            seen[s] = seen.get(s, 0) + 1
        
        return res
        