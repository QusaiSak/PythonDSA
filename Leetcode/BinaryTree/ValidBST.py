# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        curr=root
        prev = float('-inf')

        while curr:
            if curr.left is None:
                if curr.val<= prev:
                    return False
                prev = curr.val
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right!=curr:
                    pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    if curr.val<=prev:
                        return False
                    prev = curr.val
                    curr = curr.right
        return True

        