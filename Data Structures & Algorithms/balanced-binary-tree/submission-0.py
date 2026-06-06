# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # go DFS
        # explore hight
        # 
        # node is None -> 0, True
        # if diff of hights is more then 1 -> False
        # return 1 + max of heights, True

        def dfs(node):
            if node is None:
                return 0
            
            l, r = dfs(node.left), dfs(node.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1
        
        h = dfs(root)
        return h != -1