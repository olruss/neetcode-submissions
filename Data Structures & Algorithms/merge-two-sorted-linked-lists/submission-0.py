# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1->2->4
        # 1->3
        # compare head nodes. what is lower then equal goes to merged list
        # repeat until both lists is not none
        # store root node and return next
        root = ListNode()
        node = root
        while list1 or list2:
            next = None
            if list1 is None:
                next = list2
                list2 = list2.next
            elif list2 is None:
                next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                next = list1
                list1 = list1.next
            else:
                next = list2
                list2 = list2.next
            node.next = next
            node = next
        
        return root.next