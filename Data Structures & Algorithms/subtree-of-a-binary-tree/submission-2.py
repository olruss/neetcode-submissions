# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # serialization
        def tokenize(node, tokens):
            NONE = "$"
            if node is None:
                tokens.append(NONE)
                return
            tokens.append(str(node.val))
            tokenize(node.left, tokens)
            tokenize(node.right, tokens)
        
        def serialize(node):
            toks = []
            tokenize(node, toks)
            return "#".join(toks)
        
        s = serialize(subRoot)
        r = serialize(root)
        return s in r