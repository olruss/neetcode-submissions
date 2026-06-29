class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1

        largest = float('-inf')
        for n in nums:
            if cnt[n] == 1:
                largest = max(largest, n)
        
        return -1 if largest == float('-inf') else largest
