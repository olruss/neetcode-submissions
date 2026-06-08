class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [3 4 5] , 16
        #   3
        # 33             34        35
        # 333 334 335   344 345  355


        res = []
        cur = []

        def bt(i, t):
            if t == 0:
                res.append(cur.copy())
                return
            if t < 0 or i >= len(nums):
                return
            
            for j in range(i, len(nums)):
                cur.append(nums[j])
                bt(j, t - nums[j])
                cur.pop()
        
        bt(0, target)
        return res