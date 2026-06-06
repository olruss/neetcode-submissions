import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(k: int) -> int:
            return sum(math.ceil(p / k) for p in piles)
        
        min_k, max_k = 1, max(piles)

        res = max_k

        while min_k <= max_k:
            k = (min_k + max_k) // 2
            t = time(k)

            if t <= h:
                res = k
                max_k = k - 1
            else:
                min_k = k + 1
        
        return res