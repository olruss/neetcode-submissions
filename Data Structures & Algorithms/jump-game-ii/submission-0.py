class Solution:
    def jump(self, nums: List[int]) -> int:
        # 3 1 3 2 5 1 1 1 1 0
        # for every position
        # we define max jump, say for i=0, it's 3
        # then we iterate over positions we can jump to and update the
        # max jump
        # every inner loop - one jump
        # 
        # continue untill last position is reached

        jump = 0
        cnt = 0
        i = 0
        while i < len(nums):    
            for _ in range(i, jump + 1):
                if i == len(nums) - 1:
                    return cnt
                jump = max(jump, i + nums[i])
                i += 1
            
            cnt += 1
        
        return cnt
