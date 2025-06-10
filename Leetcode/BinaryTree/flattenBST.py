# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        if (root == None or root.left == None and root.right == None):
            return
        self.flatten(root.left)
        self.flatten(root.right)
        left = root.left
        right = root.right

        root.left,root.right=None,left
        curr = root
        while curr.right:
            curr=curr.right
        curr.right = right
        return root
        
        

        