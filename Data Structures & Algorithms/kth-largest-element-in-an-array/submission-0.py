import heapq

class Solution:
    # max heap (heapify the nums or create a copy if mutation is not allowed)
    # then return kth poped element
    # up to 10000 elements - max heap is ok
    # otherwise min heap would make more sense due to better efficiency
    # (array will be limited to k+1 elements)
    # 
    # time: O(N + logk), space O(N) in case of auxilary list
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)
        res = 0
        for _ in range(k):
            res = -heapq.heappop(h)
        
        return res