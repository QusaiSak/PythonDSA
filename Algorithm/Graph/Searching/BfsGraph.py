from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)  # For undirected graph

    def bfs(self, start):
        visited = set()
        q = deque([start])
        visited.add(start)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for n in self.graph[node]:
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        return res

    def BfsOfGraphDisc(self, s, visited, res):
        q = deque([s])
        visited.add(s)
        while q:
            node = q.popleft()
            res.append(node)
            for n in self.graph[node]:
                if n not in visited:
                    visited.add(n)
                    q.append(n)

    def BfsDisc(self):
        visited = set()
        res = []
        for n in self.graph:
            if n not in visited:
                self.BfsOfGraphDisc(n, visited, res)
        return res

if __name__ == "__main__":
    g = Graph()
    # Component 1
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    # Component 2
    g.add_edge(4, 5)

    print("BFS Traversal starting from node 0:", g.bfs(0))
    print("BFS Traversal of entire graph (disconnected):", g.BfsDisc())