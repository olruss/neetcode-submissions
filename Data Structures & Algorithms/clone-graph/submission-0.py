"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque


def pnode(node):
    if node is None:
        print("None")
    print(node.val, ":", "[", ",".join(str(n.val) for n in node.neighbors), "]")
    for n in node.neighbors:
        pnode(n)

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        q = deque([node])
        copies = {}
        head = None
        seen = set()
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if n in seen:
                    continue
                seen.add(n)
                if n.val not in copies:
                    copies[n.val] = Node(n.val)
                n_copy = copies[n.val]
                head = head or n_copy

                # now copy neighbours
                for nei in n.neighbors:
                    if nei.val not in copies:
                        copies[nei.val] = Node(nei.val)
                    nei_copy = copies[nei.val]
                    n_copy.neighbors.append(nei_copy)
                    q.append(nei)
        return head