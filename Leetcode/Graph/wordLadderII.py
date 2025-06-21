class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        graph = defaultdict(list)
        level={beginWord:0}
        q = deque([beginWord])
        n = len(beginWord)
        while q:
            word = q.popleft()
            for i in range(n):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordList:
                        if nextWord not in level:
                            level[nextWord] =level[word]+1
                            q.append(nextWord)
                            graph[word].append(nextWord)
                        elif level[nextWord] == level[word]+1:
                            graph[word].append(nextWord)
        res = []
        path = [beginWord]
        def dfs(w):
            if w==endWord:
                res.append(path[:])
                return 
            for nw in graph[w]:
                path.append(nw)
                dfs(nw)
                path.pop()
        dfs(beginWord)
        return res
