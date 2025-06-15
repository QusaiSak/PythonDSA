class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        def dfs(node , i):
            if i == len(word):
                return node.isLeaf 
            ch = word[i]
            if ch == '.':
                return any(dfs(c,i+1) for c in node.children.values())
            if ch not in node.children:
                return False
            return dfs(node.children[ch],i+1)
        return dfs(self.root,0)
