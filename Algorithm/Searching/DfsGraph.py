from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph

    def dfsRec(self, s, visited, res):
        visited.add(s)
        res.append(s)
        for n in self.graph[s]:
            if n not in visited:
                self.dfsRec(n, visited, res)

    def dfsDisc(self):
        visited = set()
        res = []
        count=0
        for n in self.graph:
            if n not in visited:
                count+=1
                self.dfsRec(n, visited, res)
        return res , count

    def dfs(self, start):
        visited = set()
        res = []
        self.dfsRec(start, visited, res)
        return res


if __name__ == "__main__":
    g = Graph()
    # Component 1
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)

    # Component 2
    g.add_edge(6, 7)

    print("DFS Recursive Traversal from node 0:", g.dfs(0))
    print("DFS Traversal of full disconnected graph:", g.dfsDisc())