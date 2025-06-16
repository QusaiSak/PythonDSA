class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndWord = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def insert(self,word):
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.isEndWord = True
        
        def search(self,s,start):
            curr = self.root
            pos = []
            for i in range(start,len(s)):
                if s[i] not in curr.children:
                    break
                curr = curr.children[s[i]]
                if curr.isEndWord:
                    pos.append(i+1)
            return pos

        for word in wordDict:
            insert(self,word)
        
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in search(self,s,i):
                    dp[j] = True
        return dp[len(s)]
        