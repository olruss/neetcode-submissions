import heapq


class KthLargest:

    # min heap vs max heap
    # max heap: size k. push, push, push ...
    # then get k-th element from top
    # streighforward but
    # - all elements are pushed
    # - space is O(N)
    # - return for add is tricky
    #
    # min heap:
    # heap of size k
    # push only what bigger then top
    # if size > k: push and pop on same add operation
    # top element is k-th larrgest

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k

        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]