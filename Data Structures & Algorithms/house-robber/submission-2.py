class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up
        # f(x) = max(x + x - 2, x - 1)
        # houses:  1x          2            3x         4          5x
        #     0 0| (0+0,0)1 (2+0, 1)2   (3+1,2)4   (4+2,4)6   (5+4,6) 10
        # x - decision is to rob

        h1, h2 = 0, 0
        for h in nums:
            # h1, h2 are two previous houses
            # h2 would be current house after we shift right
            h1, h2 = h2, max(
                h1 + h,  # rob
                h2,  # not to rob
            )
        
        return h2