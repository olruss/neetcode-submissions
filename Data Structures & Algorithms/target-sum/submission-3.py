class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # imagine grid
        #     min_sum <-- 0 --> max_sum
        # idx
        # 0
        # 1
        # ..

        # we start from (0, 0) base case = 1
        # one way to reach the 0 with 0 numbers
        # then for every number we apply it (- or +) for every
        # sum in prev row
        # finally result will lay in last row[target]
        #
        # as we looking on prev row only, we need only two rows
        # can be optimized to one
        # (for every value take it, and put two sums)
        #
        # or, btw, we store counters. update them when there are values
        # 
        # or, btw, now I see that one row won't work as expected
        # assume there was 1, next number is 1. when we added 1, we moved it to idx=2
        # but there is already value it can interfeer 
        # also it will be taken into account later
        # so not too much point in it

        _s = sum(nums)
        memo = [0] * (2 * _s + 1)  # -sum  0  + sum
        idx = lambda _sum: _sum + _s
        _sum = lambda i: i - _s

        if target > _s or target < -_s:
            return 0

        memo[idx(0)] = 1
        for n in nums:
            cur = [0] * len(memo)
            for i, cnt in enumerate(memo):
                if cnt == 0:
                    continue
                s = _sum(i)
                cur[idx(s - n)] += cnt
                cur[idx(s + n)] += cnt
            memo = cur
        
        return memo[idx(target)]
                