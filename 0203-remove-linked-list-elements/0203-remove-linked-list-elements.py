# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = head
        prev = None
        while dummy:
            next_node = dummy.next
            if dummy.val == val:
                if prev:
                    prev.next = dummy.next
                else:
                    head = next_node
            else:
                prev = dummy
            dummy = next_node
            
        return head
        