from TrieInit import TrieNode

def insert(root,word):
    curr = root 
    for char in word:
        idx = ord(char)-ord('a')
        if curr.children[idx] is None:
            newNode = TrieNode()
            curr.children[idx] = newNode
        curr = curr.children[idx]
    curr.isLeaf = True

def search(root,word):
    curr = root
    for char in word:
        idx = ord(char)-ord('a')
        if curr.children[idx] is None:
            return False
        curr = curr.children[idx]
    return curr.isLeaf

def prefixSearch(root,prefix):
    curr = root
    for char in prefix:
        idx = ord(char)-ord('a')
        if curr.children[idx] is None:
            return False
        curr = curr.children[idx]
    return True  



#Example
root = TrieNode()
insert(root, "hello")
insert(root, "world")
insert(root, "hi")
insert(root, "trie")
insert(root, "tree")
insert(root, "data")
print("Words inserted successfully.")
# print("Root children:", [chr(i + ord('a')) for i, child in enumerate(root.children) if child is not None])
print("Searching for 'hello':", search(root, "hello"))
print("Searching for 'world':", search(root, "world"))
print("Searching for 'hi':", search(root, "hi"))
print("Searching for 'tri':", search(root, "tri"))

#Prefix Search
print("Prefix search for 'tr':", prefixSearch(root, "tr"))
print("Prefix search for 'he':", prefixSearch(root, "he"))
print("Prefix search for 'da':", prefixSearch(root, "da"))
print("Prefix search for 'xyz':", prefixSearch(root, "xyz"))