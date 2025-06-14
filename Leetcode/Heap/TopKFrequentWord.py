class Solution(object):
    def topKFrequent(self, words, k):
        wordmap = {}
        for word in words:
            if word in wordmap:
                wordmap[word] += 1
            else:
                wordmap[word] = 1
        
        heap=[]
        for word , freq in wordmap.items():
            heapq.heappush(heap,(-freq,word))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result