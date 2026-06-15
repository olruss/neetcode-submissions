class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # for every given number
        # we can include or not include into array
        # do until half of sum is exceeded or index is out of bound
        # if current sum equal to target -> win

        nums.sort()
        s = sum(nums)
        if s % 2 != 0:
            return False
        half = s / 2

        def dfs(i, cur):
            if cur == half:
                return True
            if cur > half or i >= len(nums):
                return False
            
            res = dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)
            return res

        return dfs(0, 0)

