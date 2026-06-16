class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # average is a sum / number of elements
        # algo:
        # calculate prefix sum for every element
        # store in array of same lengh as arr
        # then iterate with fixed window of lengh k
        # sum of the array elements would be
        # prefix sum of right element - pref sum of element to the left of the window
        # sum / k = average
        # compare with threshold
        # increase the counter
        # 
        # O(N) time and space
        #
        # let's trace over 
        #   [1 2 3 1 1], k = 3, threshold=2
        # ps 1 3 6 7 8
        # 1  |   |  6-0 / 3 = 2 -> ok
        # 2    |   | 7 - 1 / 3 = 2 -> ok
        # 3      |    |  8 - 3 / 3 < 2 -> nok
        # result - 2

        sums = [0] * len(arr)
        _s = 0
        for i, n in enumerate(arr):
            _s += n
            sums[i] = _s

        l, r = 0, k - 1

        res = 0
        while r < len(arr):
            sub_sum = sums[r] - (
                sums[l - 1]
                if l > 0 else 0
            )
            if sub_sum / k >= threshold:
                res += 1
            l += 1
            r += 1
        
        return res


