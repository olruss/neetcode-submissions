class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [20, 18, 19, 25, 2] -> [3, 1, 1, 0, 0]
        # brute force:
        # for every element go right until day with higher temperature reached
        # repeat for every single day
        # O(N^2)
        # ---
        res = [0] * len(temperatures)
        i = 0
        while i < len(temperatures) - 1:
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                j += 1
            if j < len(temperatures):
                res[i] = j - i
            i += 1
        return res