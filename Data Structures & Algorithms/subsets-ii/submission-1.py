class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort
        # for every right (non include) decision
        # skip duplicates
        
        # [2 1 2] -> [1 2 2]
        #                     0[1]              0[]
        #            1[1 2]         3[1]x    1[2]      3x[]
        #        2x[1 2 2]  3x[1 2]         2[2 2]  3x[2]
        # x - exit
        # Nx, N - current index

        res = []
        cur = []
        nums.sort()
        def bt(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            # include
            cur.append(nums[i])
            bt(i + 1)
            # not include, skip duplicates
            cur.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            
            bt(i + 1)
        
        bt(0)
        return res