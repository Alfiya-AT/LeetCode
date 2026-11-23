# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        
        def dfs(node):
            if not node:
                return 0,None

            dl,nl = dfs(node.left)
            dr,nr = dfs(node.right)

            if dl>dr:
                return dl+1,nl

            if dr>dl:
                return dr+1,nr

            return dl+1,node

        return dfs(root)[1]