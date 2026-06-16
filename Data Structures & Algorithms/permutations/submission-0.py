class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #            (123)
        #      1         2         3
        #     (23       31         12)
        #   2     3   3     1   1     2
        #  
        #   3     2   3     1   1     2

        # go dfs()
        # until nums is not empty
        # on every round we iterate through remaining array
        # pop left, then append to right when backtrack

        res = []
        cur = []

        def dfs():
            if not nums:
                res.append(cur.copy())
                return
            for _ in range(len(nums)):
                cur.append(nums.pop(0))
                dfs()
                nums.append(cur.pop())
        
        dfs()
        return res