class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # naive approach:
        # take one number, then solve two-sum for remaining
        # two sum -> O(n) => O(n**2)
        # prevent duplicates - set of tuples

        # smarter - sort first
        # then take element and solve two-sum for sorted 
        # O(NlogN)
        # prevent duplicates - skip seen numbers


        # [-4, -1, -1, 0, 1, 2]


        snums = sorted(nums)
        
        def _two_sum(i):
            res = []
            target, l, r = -snums[i], i + 1, len(snums) - 1
            r = len(nums) - 1
            while l < r:
                s = snums[l] + snums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([snums[l], snums[r]])
                    r -= 1
                    l += 1
                    while l < len(snums) and snums[l-1] == snums[l]:
                        l += 1
                    while r >= 0 and snums[r + 1] == snums[r]:
                        r -= 1

            return res
            
        triplets = []

        i = 0
        while i < len(snums) - 2:
            if i > 0 and snums[i] == snums[i-1]:
                i += 1
                continue
            ts_res =  _two_sum(i)
            for r in ts_res:
                triplets.append([snums[i], *r])
            i += 1
        
        return triplets