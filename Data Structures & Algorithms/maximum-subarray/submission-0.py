class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # subarray is growing until it's current sum
        # (sum of elements from the start of sub-array)
        # is positive
        #
        # so we can go left to right, calculate current sum
        # when it's negative - drop to 0 and continue
        # on every turn update the max

        res = min(nums)
        cur = 0
        for n in nums:
            cur += n
            res = max(res, cur)
            if cur < 0:
                cur = 0
        return res