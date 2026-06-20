import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # usually it would be Dijksta
        # but with k stops restriction it won't work
        # as we can't update the score for visited node
        # 
        # but wait, what if we include number of stops
        # to every node we put in queue
        # and skip those pathes, where number of stops exceeded k
        # well, it should work. lets code this up

        adj = {i: [] for i in range(n)}
        for f, t, dist in flights:
            adj[f].append((t, dist))
        
        # (distance, stops, node)
        q = []
        q.append((0, src, -1))
        visited = {}

        while q:
            dist, a, stops = heapq.heappop(q)
            if stops > k:
                continue
            # if a == dst:
            #     break
            if (a, stops) in visited:
                continue
            visited[(a, stops)] = dist

            for b, dis in adj[a]:
                if b not in visited:
                    heapq.heappush(q, (dist + dis, b, stops + 1))
        
        res = float("inf")
        for i in range(k + 1):
            if (dst, i) in visited:
                res = min(res, visited[(dst, i)])
        return  -1 if res == float("inf") else res
