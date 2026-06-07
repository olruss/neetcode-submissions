# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        
        if not root.right and not root.left:
            return None
        
        if not root.right:
            return root.left
        
        if not root.left:
            return root.right
        
        successor = root.right
        while successor.left:
            successor = successor.left
        
        self.deleteNode(root, successor.val)
        root.val = successor.val

        return root
        