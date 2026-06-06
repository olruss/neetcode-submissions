# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # go dfs
        # for every node max diameter is max depth left + max depth right + 1
        # update max diameter and return max depth
        
        #     1
        #  2      3
        # 4  5
        #      6
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            
            depth_left = dfs(node.left)
            depth_right = dfs(node.right)
            res = max(res, depth_left + depth_right)

            return max(depth_left, depth_right) + 1
        
        dfs(root)
        return res