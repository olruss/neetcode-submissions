class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we can iterate left to right
        # and update the max possible jump
        
        jump = 0
        for i in range(len(nums)):
            if jump < i:
                return False
            jump = max(jump, i + nums[i])
        return True