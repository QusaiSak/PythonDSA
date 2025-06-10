from collections import deque
# Connected Graph using Adjacency List Representation
def BFS(G , S):
    V = len(G)
    res = []
    visited = [False] * V
    q = deque()
    
    q.append(S)
    visited[S] = True
    while q:
        node = q.popleft()
        res.append(node)
        
        for x in G[node]:
            if not visited[x]:
                visited[x]=True
                q.append(x)
    return res

#Disconnected Graph using Adjacency List Representation
def BFS_Disconnected(G):
    V = len(G)
    res = []
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = True
            while q:
                node = q.popleft()
                res.append(node)
                for x in G[node]:
                    if not visited[x]:
                        visited[x] = True
                        q.append(x)     
    return res

# Example usage
G = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
S = 0
print("BFS Traversal of Connected Graph:", BFS(G, S))
G_disconnected = {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}
print("BFS Traversal of Disconnected Graph:", BFS_Disconnected(G_disconnected))


