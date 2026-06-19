class Solution:
    def search(self, nums: List[int], target: int) -> int:      
        # target: 2
        # 3 4 5 6 1 2
        # 5 6 1 2 3 4
        # 8 1 2 3 4 5 6 7
        #
        # half of the array will be sorted
        # so we can check the sorted part first
        # if number is there, then drop other
        # or drop sorted part

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            v = nums[mid]

            if v == target:
                return mid
            
            # right part is sorted
            if v < nums[r]:
                if target > v and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # left is sorted
            else:
                if target < v and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
