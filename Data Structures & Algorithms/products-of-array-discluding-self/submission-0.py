class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #    [1, 2, 4, 6]
        # [1, 1, 1, 1, 1, 1]
        products_right = [1] * (len(nums))
        products_left = [1] * (len(nums))

        lp, rp = 1, 1
        
        # products of elements to the left
        for i in range(len(nums)):
            products_left[i] = lp
            lp *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            products_right[i] = rp
            rp *= nums[i]
        
        res = [products_right[i] * products_left[i] for i in range(len(nums))]
        return res