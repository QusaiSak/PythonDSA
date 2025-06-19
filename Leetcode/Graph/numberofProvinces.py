class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            if n1!=par[n1]:
                par[n1] = find(par[n1])
            return par[n1]

        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2]+=rank[p1]
            else:
                par[p2] = p1
                rank[p1]+=rank[p2]
            return 1
        res = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    res-=union(i,j)
        return res