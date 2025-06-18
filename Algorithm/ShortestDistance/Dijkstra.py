import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    pre = [-1] * n
    pre[start] = start  
    pq = [(0, start)]  # (distance, node)
    while pq:
        d, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        if d > dist[node]:
            continue
        for n, w in graph[node]:
            if (dist[n] == float('inf') or dist[node] + w < dist[n]) and not visited[n]:
                dist[n] = dist[node] + w
                pre[n] = node
                heapq.heappush(pq, (dist[n], n))
    def get_path(node):
        if node == -1 or dist[node] == float('inf'):
            return []
        path = []
        while node != start:
            path.append(node)
            node = pre[node]
        path.append(start)
        return path[::-1]  # Reverse the path to get it from start to node
    paths = [get_path(i) for i in range(n)]
    return dist, paths
    

if __name__ == "__main__":
    # Larger connected graph represented as an adjacency list
    graph = [
        [(1, 4), (2, 3), (3, 7)],           # Node 0: connections to 1, 2, 3
        [(0, 4), (2, 6), (4, 3)],           # Node 1: connections to 0, 2, 4
        [(0, 3), (1, 6), (3, 2), (5, 8)],   # Node 2: connections to 0, 1, 3, 5
        [(0, 7), (2, 2), (4, 5), (6, 9)],   # Node 3: connections to 0, 2, 4, 6
        [(1, 3), (3, 5), (5, 4), (7, 7)],   # Node 4: connections to 1, 3, 5, 7
        [(2, 8), (4, 4), (8, 2)],           # Node 5: connections to 2, 4, 8
        [(3, 9), (7, 3), (8, 6)],           # Node 6: connections to 3, 7, 8
        [(4, 7), (6, 3), (9, 5)],           # Node 7: connections to 4, 6, 9
        [(5, 2), (6, 6), (9, 8)],           # Node 8: connections to 5, 6, 9
        [(7, 5), (8, 8)]                     # Node 9: connections to 7, 8
    ]
    
    start = 0
    print("Graph representation (adjacency list):")
    for i, edges in enumerate(graph):
        print(f"Node {i}: {edges}")
    
    distances, paths = dijkstra(graph, start)
    print(f"\nShortest distances from node {start} to all other nodes:")
    for i, (distance, path) in enumerate(zip(distances, paths)):
        if distance == float('inf'):
            print(f"Node {i}: Not reachable")
        else:
            print(f"Node {i}: Distance = {distance}, Path = {path}")
    
    