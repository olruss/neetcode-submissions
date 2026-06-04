class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # test cases:
        # [] -> 0
        # [1] -> 0
        # [2, 3] -> 2
        # [1,4,5,1] -> 4


        #    [1, 4, 5, 1]
        # 1:  |        |    -> (3-0) * 1 -> 3
        # 2:  |     |<-     -> (2-0) * 1 -> 2
        # 3:  -> |  |       -> (2-1) * 4 -> 4
        def vol(l, r):
            return (r - l) * min(heights[r], heights[l])
        
        l, r = 0, len(heights) - 1

        max_vol = 0
        while l < r:
            max_vol = max(max_vol, vol(l, r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_vol