# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0->1->2->3->None ===> 3->2->1->0->None
        dummy = ListNode()

        def reverse(node):
            if node is None:
                return dummy
            n = reverse(node.next)
            n.next = node
            node.next = None
            return node
        
        reverse(head)
        return dummy.next