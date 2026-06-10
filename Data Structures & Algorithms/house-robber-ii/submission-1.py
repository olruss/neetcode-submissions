class Solution:
    def rob(self, nums: List[int]) -> int:
        # in order two break the chain,
        # instead of houses placed in circle
        # we imagine two lines 
        # 1. first - last -1 (can rob first house)
        # 2. second - last (can't rob first house)
        # then just pick max from those

        def calc(l, r):
            a, b = 0, 0
            for i in range(l, r):
                a, b = b, max(
                    b,
                    a + nums[i]
                )
            return b
        # corner case:
        # one house
        if len(nums) == 1:
            return nums[0]
            
        return max(
            calc(0, len(nums) - 1),
            calc(1, len(nums))
        )
