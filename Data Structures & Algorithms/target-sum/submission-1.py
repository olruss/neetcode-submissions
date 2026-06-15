class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DFS
        # add or substract
        # go until index is exceeded
        # memo key = (i, target)

        memo = {}

        def dfs(i, trgt):
            if (i, trgt) in memo:
                return memo[(i, trgt)]
            if i == len(nums) and trgt == target:
                return 1
            if i >= len(nums):
                return 0

            res = 0
            # add
            res += dfs(i + 1, trgt + nums[i])
            # subtract
            res += dfs(i + 1, trgt - nums[i])
            
            memo[(i, trgt)] = res
            return res

        return dfs(0, 0)