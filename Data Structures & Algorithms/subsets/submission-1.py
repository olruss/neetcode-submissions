from collections import deque

class Solution:
    # 3241
    # 241 413 132 324
    # 41 12 24 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we are forming a binary tree:
        # include or not include
        #                       [1 2 3]
        # 1:            [1]                        []
        # 2:      [1 2]      [1]             [2]       []
        # 3: [1 2 3] [1 2]  [1 3]  [1]  [2 3]   [2]  [3]  []

        # number of combinations: 2^N
        # time: 2^N. space: N (hight of tree)

        res = []
        cur = []
        def bt(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            # include
            cur.append(nums[i])
            bt(i + 1)
            # not include
            cur.pop()
            bt(i + 1)
        bt(0)
        return res