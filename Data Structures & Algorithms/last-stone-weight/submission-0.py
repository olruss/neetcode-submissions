import heapq


class Solution:
    # max heap
    # heapify
    # then until there are at least 2 stones:
    # pop them, merge and push if stone left
    # return what's left
    # 
    # complexity O(N) for heapyfy + O(NlogN) for pop/push => NlogN
    # no extra space, if we mutate the initial list. otherwise O(N)

    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)  # max heap
        
        while len(h) >= 2:
            x, y = -heapq.heappop(h), -heapq.heappop(h)
            if x == y:
                continue
            # max heap, so x > y
            heapq.heappush(h, y-x)
        
        return -h[0] if h else 0