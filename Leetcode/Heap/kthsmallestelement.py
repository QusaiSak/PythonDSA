class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap,-matrix[i][j])
        n = len(heap)
        for i in range(n):
            if len(heap)>k:
                heapq.heappop(heap)

        return -heap