from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle  found - can't complete
        # course is complete when no prerequisites left

        adj = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            adj[c].append(p)

        completed = set()
        seen = set()

        def dfs(i):
            if i in seen:
                return False
            if i in completed:
                return True
            prerequisites = adj[i]
            if len(prerequisites) == 0:
                completed.add(i)
                return True
            
            seen.add(i)
            for preq in prerequisites:
                res = dfs(preq)
                if not res:
                    return False
            seen.remove(i)
            completed.add(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
