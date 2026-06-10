import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap version
        # time: O(NlogN), space O(N)

        # with min heap can be optimized to O(NlogK) time

        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1

        h = []
        for n, c in cnt.items():
            heapq.heappush(h, (c, n))
            if len(h) > k:
                heapq.heappop(h)
        
        return [el[1] for el in h]