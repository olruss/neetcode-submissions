# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []
        # q = [root]
        # while q:
        # cur = []
        # for _ in range len st ->
        #   take node from qeue, if not None, put val in cur and add left and right to queue
        #   if cur lengh > 0 -> append to res
        # [1, 3, 5, null, 6] -> [[1], [3, 5], [6]]
        # 
        # O(N), O(N)
        res = []
        q = [root]

        while q:
            cur = []

            for _ in range(len(q)):
                node = q.pop(0)
                if node is None:
                    continue
                
                cur.append(node.val)
                q.append(node.left)
                q.append(node.right)
            
            if cur:
                res.append(cur)
        
        return res
        
        