class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # l, r - boundaries of window of variable size
        # on every itteration calculate sum of subarray
        # and update result when it hit the target
        # if sum is greater - move l right
        # if it is lower - move r right

        l, r = 0, 0
        _sum = nums[0]
        res = float('inf')
        #   1 8 10 1 ; 10
        #   ||          1
        #   | |         9
        #   |    |      19 -> 3
        #     |  |      18 -> 2
        #        ||     10 -> 1
        #          ||   1

        while r < len(nums):
    
            if _sum >= target:
                res = min(res, r - l + 1)
                _sum -= nums[l]
                l += 1
            else:
                r += 1
                if r < len(nums):
                    _sum += nums[r]
            if l > r:
                r = l

        return res if res != float('inf') else 0
        