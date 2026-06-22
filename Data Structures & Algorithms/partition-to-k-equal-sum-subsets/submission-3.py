class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # create k buckets [0] * k
        # for every given number we will have to choose
        # what bucket to put it on
        # so it will be our DFS decision
        
        s = sum(nums)
        if s % k != 0:
            return False

        target = s // k
        buckets = [0] * k

        def dfs(i):
            if i >= len(nums):
                return True
            
            for j in range(k):
                # no need to try same buckets more then once
                if j > 0 and buckets[j] == buckets[j - 1]:
                    continue
                if nums[i] + buckets[j] <= target:
                    buckets[j] += nums[i]
                    res = dfs(i + 1)
                    if res:
                        return True
                    buckets[j] -= nums[i]
            return False
        
        # nums.sort(reverse=True)
        res = dfs(0)
        return res
