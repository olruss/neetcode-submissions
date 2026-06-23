class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # i can go dfs(i, j) indexing both words
        # it should return number of actions I need to perform
        # to reach the base case
        # base case - both indexes are out of range
        #
        # on every turn I have desicions to make:
        # 0) skip if letters are equal dfs(i+1, j+1)
        # 1) delete charecter 1 + dfs(i+1, j)
        # 2) add charecter 1 + dfs(i + 1, j + 1)
        # 3) replace charecter
        #    - I can replace only if word2[j] in word1[i:]
        #    - But I think I have to try to do all possible replacements
        #      assuming this: kara ark
        #      i can replace 1-0 and have akra
        #      or I 3-0 and have aark wich moves me closer
        #
        # I will return minimum result of all possible choices
        # it can be stored in memory[(i, j)]

        memo = {}

        def dfs(i, j):
            if i >= len(word1) and j >= len(word2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                i += 1
                j += 1

            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            
            res = float('inf')
            # insert
            res = min(res, dfs(i, j+1))
            # delete
            res = min(res, dfs(i+1, j))
            # replace
            res = min(res, dfs(i+1, j+1))
            # all those actions cost 1
            res += 1

            memo[(i, j)] = res

            return res

        return dfs(0, 0)

