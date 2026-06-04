class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort -> NlogN
        seen = set(nums)

        res = 0
        cur = 0

        for n in nums:
            while n in seen:
                cur += 1
                n += 1
            res = max(res, cur)
            cur = 0
        
        return res