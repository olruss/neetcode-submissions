class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # count current sum, drop to 0 when it's neagative,
        # update on every turn
        #
        # what makes it special: the circularity
        # but we can track the last reset
        # and after we finished, just continue until
        # last reset index or next sum drop
        #
        # -- discovered after faild submission --
        # reset logic won't work
        # we should reset index if element is negative
        # [5, -3, 5]
        # we will reset on 1
        # then we will start from it and do the loop
        # until i is less then 1
        #
        # -- one more failed submission
        # oh, I think here is a completely different solution
        # and to be honest, I think I seen it somewhere in the past
        # idea is that we can calculate the max continious decreasing subsequence
        # and then just substract it from the max subarray
        # 
        # should work, but can't proof

        # -- also fails
        # damn

        sum_total = 0
        sum_max = nums[0]
        cur_max = 0
        sum_min = nums[0]
        cur_min = 0

        for i, n in enumerate(nums):
            sum_total += n
            cur_max += n
            cur_min += n
            sum_max = max(sum_max, cur_max)
            sum_min = min(sum_min, cur_min)

            if cur_max < 0:
                cur_max = 0
            if cur_min > 0:
                cur_min = 0

        return max(sum_max, sum_total - sum_min) if sum_min != sum_total else sum_max