# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val = None):
            if node is None:
                return 0
            if max_val is None:
                max_val = node.val

            is_good = node.val >= max_val
            max_val = max(node.val, max_val)
            return (
                int(is_good)
                + dfs(node.left, max_val)
                + dfs(node.right, max_val)
            )
        
        return dfs(root)