class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # two pointers: 0, 1
        # move right pointer in for loop
        # move left pointer to current right position
        # when r num == r-1 num or previous comparison sign
        # different from curren
        #
        # comparison r > r-1 -> 1 , r < r-1 -> 0
        
        prev = -1
        res = 1
        cnt = 1
        for r in range(1, len(arr)):
            if arr[r-1] == arr[r]:
                cnt = 1
            elif int(arr[r] > arr[r-1]) == prev:
                cnt = 2
            else:
                cnt += 1
            prev = int(arr[r] > arr[r-1])
            res = max(res, cnt)

        return res

