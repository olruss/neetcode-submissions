class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1, 2] 2
        # 0, 3 , 1 
        # 1, 3 , 
        
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1