class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford
        # for every node we will track the distance to reach it
        # and tmp distance on every turn
        # starting with 0 for src and inf for others
        # 
        # then on every turn we will go through all the edges
        # and update the tmp distances first, and then merge with distances
        # 
        # in general, it should be repeated untill no updates happend
        # but in our case turns are restrcited by k + 1

        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices.copy()
            for a, b, d in flights:
                if prices[a] != float('inf'):
                    tmp[b] = min(tmp[b], prices[a] + d)
            for i in range(len(prices)):
                prices[i] = min(prices[i], tmp[i])
        
        return prices[dst] if prices[dst] != float("inf") else -1