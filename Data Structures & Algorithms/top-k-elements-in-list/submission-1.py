class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums))]

        for n, cnt in count.items():
            buckets[cnt-1].append(n)
        
        res = []
        while len(res) < k:
            res.extend(buckets.pop())
        return res[:k]

