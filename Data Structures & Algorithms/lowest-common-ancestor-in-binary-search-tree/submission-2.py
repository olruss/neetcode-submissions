# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dfs
        
        def dfs(node):
            if node is None:
                return None
            
            if max(p.val, q.val) < node.val:
                return dfs(node.left)
            if min(p.val, q.val) > node.val:
                return dfs(node.right)
            return node
        
        return dfs(root)