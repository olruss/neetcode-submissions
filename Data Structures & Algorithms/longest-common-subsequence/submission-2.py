class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom-up
        #   0 c r a b t
        # 0 0 0 0 0 0 0
        # c 0 1 1 1 1 1
        # a 0 1 1 2 2 2
        # t 0 1 1 2 2 3
        #
        # on each run we will compare chars:
        # if match, we will increase prev val dp[i-1][j-1] + 1
        #   for example when checking a, we shoud get back
        #   to previous state c vs cr where we had 1 and
        #   add matched letter a to get "ca", "cra" (+1)
        # oterwise we take max(left, upper)
        #   say we checking a with b - no match
        #   to the left is match "ca" vs "cra" -> 2
        #   on top is match "c" vs "crab" -> 1
        #   we pick 2

        dp = [0] * (len(text2) + 1)
        
        for c in text1:
            tmp = dp[:]
            for j in range(1, len(text2) + 1):
                if c == text2[j-1]:
                    tmp[j] = 1 + dp[j-1]
                else:
                    tmp[j] = max(dp[j], tmp[j-1])
            dp = tmp[:]
        
        return dp[-1]