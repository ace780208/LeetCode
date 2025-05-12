# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sec = head
        fast = head
        prev = None
        while(fast and fast.next):
            prev = sec
            sec = sec.next
            fast = fast.next.next
        
        next_node = sec.next
        if prev:
            prev.next = next_node
        else:
            return None
        return head
        