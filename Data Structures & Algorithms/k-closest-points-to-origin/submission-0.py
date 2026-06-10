import heapq
from math import sqrt

def distance(a, b):
    return sqrt(a**2 + b**2)

class Solution:

    # max heap:
    # push. if len heap > k: pop
    # all elements in heap - k closest
    # Complexity: O(Nlogk), space O(k)

    # min heap:
    # heapify, then get top k points
    # Complexity O(N+ klogN) . space O(N) if extra is used (or mutate original list)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [
            (distance(*p), p[0], p[1])
            for p in points
        ]
        heapq.heapify(h)
        res = []
        for _ in range(k):
            p = heapq.heappop(h)
            res.append([p[1], p[2]])
        
        return res