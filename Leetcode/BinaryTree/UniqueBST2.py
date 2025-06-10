# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        dp = {}
        def dfs(l,r):
            if l>r:
                return [None]
            if (l,r) in dp:
                return dp[(l,r)]
            ans=[]
            for ro in range(l,r+1):
                for ln in dfs(l,ro-1):
                    for rn in dfs(ro+1,r):
                        rootN = TreeNode(ro,ln,rn)
                        ans.append(rootN)
            dp[(l,r)] = ans
            return ans
        return dfs(1,n)

            
        