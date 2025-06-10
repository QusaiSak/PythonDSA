# Binary Tree 
# It is a non-linear and hierarchical data structure where each node has at most two children referred to as the left child and the right child.  The topmost node in a binary tree is called the root, and the bottom-most nodes are called leaves.

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None