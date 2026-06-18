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
        #
        # we can make it more efficient
        # by comparing graph hights
        # and adding smaller graph to higher, so we have more efficient search

        parents = {}

        def find(v):
            h = 1
            while v in parents:
                v = parents[v]
                h += 1
            return v, h
        
        for a, b in edges:
            pa, ha = find(a)
            pb, hb = find(b)

            if pa == pb:
                return [a, b]
            if ha > hb:
                # attach graph B to A if it's lower
                parents[pb] = pa
            else:
                parents[pa] = pb
    