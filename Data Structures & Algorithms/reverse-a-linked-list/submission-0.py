# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3 -> None
        # prev=None, node=0; 0 -> None; node = 1, prev = 0

        prev, node = None, head
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        
        return prev