class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DFS
        # index both strings
        # base case - index out of range. return 0
        # when chars are equal - just increment both indexes
        # and count +1
        # then we have two decisions:
        # - skip char (kind a remove) for text1
        # - skip for text2
        # we will take max of that
        # 
        # this is a 2DP
        # memo key is (i, j)

        memo = {}

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                res = 1 + dfs(i+1, j+1)
            else:
                res = max(
                    dfs(i+1, j),
                    dfs(i, j+1)
                )
            memo[(i, j)] = res
            return res

        return dfs(0, 0)
