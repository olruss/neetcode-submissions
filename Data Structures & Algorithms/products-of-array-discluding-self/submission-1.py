class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #    [1, 2, 4, 6]
        res = [1] * (len(nums))

        lp, rp = 1, 1
        
        # products of elements to the left
        for i in range(len(nums)):
            res[i] = lp
            lp *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rp
            rp *= nums[i]
        
        return res