class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if (m := target - n) in seen:
                return [seen[m], i]
            seen[n] = i
        return [-1, -1]
