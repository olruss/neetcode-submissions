class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # let's apply union find
        # the idea is that we assume that we start from independent graphs
        # then we joining them 
        #
        # we have dict with child-parrent mapping
        # parent maps to itself
        # so for every child we will be able to find it's parent
        #
        # this map will store all the graphs
        # when new edge is proccessing
        # if roots are different, we join them
        # say we already have 1-2-3 and adding 3-4
        # in this case we find that 3 connected to 1 but 4 is root node itself
        # so we connect 4 to root of 3 (union them)
        # 
        # LOOP DETECTION
        # if both verticies point to same root, 
        # then it's a loop

        parents = {}

        def find(v):
            while v in parents:
                v = parents[v]
            return v
        
        for a, b in edges:
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return [a, b]
            parents[pa] = pb
    