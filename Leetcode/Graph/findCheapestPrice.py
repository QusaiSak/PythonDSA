class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        pq = deque([(0,src,0)])
        prices = [float('inf')]*n
        prices[src] = 0
        while pq:
            cost,node,stops = pq.popleft()
            if stops>k:
                continue
            for nei , c in graph[node]:
                newCost = c+cost
                if newCost < prices[nei]:
                    prices[nei] = newCost
                    pq.append((newCost,nei,stops+1))

        return prices[dst] if prices[dst] != float('inf') else -1
