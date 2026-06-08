class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def bt(i):            
            if len(cur) == k:
                res.append(cur.copy())
                return
            if n - i + 1 < k - len(cur):
                return
            
            for v in range(i, n + 1):
                cur.append(v)
                bt(v + 1)
                cur.pop()
            
        bt(1)
        return res