class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # same as subsets:
        # - include or not include
        # but stop when lenght is = k
        #
        # time complexity: 2^N, space - N

        res = []
        cur = []

        def bt(i):
            if len(cur) == k:
                res.append(cur.copy())
                return
            if n - i + 1 < k - len(cur):
                return
            
            # include
            cur.append(i)
            bt(i + 1)
            # not include
            cur.pop()
            bt(i + 1)
        
        bt(1)
        return res
    
            