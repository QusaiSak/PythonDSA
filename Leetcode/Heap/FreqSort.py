class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        maxHeap = [(-f,w) for w,f in freq.items()]
        heapq.heapify(maxHeap)
        res = []
        while maxHeap:
            f , w = heapq.heappop(maxHeap)
            res.append(w*-f)
        return ''.join(res)
