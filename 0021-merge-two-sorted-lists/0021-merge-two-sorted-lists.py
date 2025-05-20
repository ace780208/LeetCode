# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        p1 = list1
        p2 = list2
        head = ListNode(-101)
        dummy = head
        while p1 and p2:
            if p1.val >= p2.val:
                dummy.next = ListNode(p2.val)
                p2 = p2.next
            else:
                dummy.next = ListNode(p1.val)
                p1 = p1.next
            dummy = dummy.next
        
        while p1:
            dummy.next = ListNode(p1.val)
            dummy = dummy.next
            p1 = p1.next
        
        while p2:
            dummy.next = ListNode(p2.val)
            dummy = dummy.next
            p2 = p2.next
        
        return head.next