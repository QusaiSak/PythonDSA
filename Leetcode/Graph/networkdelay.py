
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v , c in times:
            graph[u].append((v,c))
        q = [(0,k)]
        heapq.heapify(q)
        visited = set()
        price = [float('inf')] * (n+1)
        price[k] = 0
        minDis = 0
        while q:
            cost,node=heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            minDis = cost
            for nei , c in graph[node]:
                newCost = c+cost
                if newCost < price[nei]:
                    price[nei] = newCost
                    heapq.heappush(q,(newCost,nei))
        return minDis if len(visited) == n else -1
