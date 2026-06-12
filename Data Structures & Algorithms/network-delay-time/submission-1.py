import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # for every node we can track how much distance
        # it will require to cover
        # to reach the node
        # we can go BFS
        # and every time we reach the node, we will update the min distance for that node
        # when pushing to queue, we should store current distance for this node
        #
        # but wait, what if we have graph like
        # 1 -> 2 -> 3 -> 4
        # 1 -> 3
        # assume 1-3 is length 4, other 1
        # if we go BFS, then 3 will be covered on first turn
        # we will update it later, but 1-2-3 will break cuz 3 in seen
        # so we won't reach 4 by shortest path and will never update it
        #
        # I think we can solve it by not tracking visited nodes
        # but visited edges
        # so we will push edges in queue
        # for our example:
        # 1-2:1, 1-3:4. (1:0, 2:1, 3:4)
        # 2-3:2, 3-4:4  (1:0, 2:1, 3:2, 4:4)
        # 3-4:3.        (1:0, 2:1, 3:2, 4:3)
        # Solved !!!


        # But wait,
        # why should we visit all the pathes
        # we got two edjest that lead us to 4: 3-4 and 1-3. we could just pick the smallest one
        # so we can go Gridy here and actually use min heap here, not bfs
        # so just pick the edje based on shortest path
        # on every turn until all nodes are visited
        # 
        # Let's code this up

        # first we need to create an adjucency list for our graph
        # adj = {node: [(dist, nei), ...], ...: ...}
        adj = {i: [] for i in range(1, n + 1)}
        for t in times:
            adj[t[0]].append((t[2], t[1]))
        
        
        visited = {k: 0}
        q = []

        # add starting point to q
        for nei in adj[k]:
            heapq.heappush(q, nei)

        while q and len(visited) < n:
            dist, node = heapq.heappop(q)
            if node in visited:
                continue
            visited[node] = dist
            
            for nei in adj[node]:
                heapq.heappush(q, (nei[0] + dist, nei[1]))
            
        return -1 if len(visited) < n else max(visited.values())
