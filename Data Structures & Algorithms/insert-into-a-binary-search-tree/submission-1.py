# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        new_leaf = TreeNode(val)

        if not root:
            return new_leaf

        while node != new_leaf:
            if val > node.val:
                node.right = node.right or new_leaf
                node = node.right
            elif val < node.val:
                node.left = node.left or new_leaf
                node = node.left
            else:
                break
        
        return root
                