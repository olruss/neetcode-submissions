class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            adj[c].append(p)
        
        visited = set()
        taken = []

        def dfs(c):
            if c in visited:
                return False
            if c in taken:
                return True

            visited.add(c)
            for pc in adj[c]:
                res = dfs(pc)
                if not res:
                    return False
            
            visited.remove(c)
            taken.append(c)
            return True
        
        for i in range(numCourses):
            r = dfs(i)
            if not r:
                return []

        return taken