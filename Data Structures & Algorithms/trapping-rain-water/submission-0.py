class Solution:
    def trap(self, height: List[int]) -> int:
        left_heights = [0] * len(height)
        max_l = 0
        for i in range(len(height)):
            left_heights[i] = max_l
            max_l = max(max_l, height[i])
        
        max_r = 0
        total = 0
        for i in range(len(height) -1, -1 , -1):
            vol = max(0, min(left_heights[i], max_r) - height[i])
            total += vol
            max_r = max(max_r, height[i])
        
        return total



