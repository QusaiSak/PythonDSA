class TrieNode:
        def __init__(self):
            self.children = [None]*26
            self.isLeaf = False
            self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        r = len(board)
        c = len(board[0])
        result = []
        root = TrieNode()
        def insert(word):
            curr = root
            for c in word:
                idx = ord(c) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
            curr.isLeaf = True
            curr.word = word

        def findWord(i,j,root):
            ch = board[i][j] 
            if (ch == '$' or root.children[ord(ch) - ord('a')] is None):
                return
            next_node = root.children[ord(ch) - ord('a')]
            if next_node.isLeaf == True:
                result.append(next_node.word)
                next_node.isLeaf = False
            board[i][j] = '$'
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni,nj=i+dx,j+dy
                if 0<=ni<r and 0<=nj<c:
                    findWord(ni,nj,next_node)
            board[i][j] = ch
                
        for word in words:
            insert(word)

        for i in range(r):
            for j in range(c):
                findWord(i,j,root)

        return result