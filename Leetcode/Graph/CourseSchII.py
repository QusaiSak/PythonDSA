# Used Kahn's Algo

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        for d,s in prerequisites:
            graph[s].append(d)
            inDegree[d]+=1
        q = deque([i for i in range(numCourses) if inDegree[i]==0])
        res = []
        while q :
            node = q.popleft()
            res.append(node)
            for n in graph[node]:
                inDegree[n]-=1
                if inDegree[n]==0:
                    q.append(n)
        if len(res) == numCourses:
            return res
        else:
            return []  

