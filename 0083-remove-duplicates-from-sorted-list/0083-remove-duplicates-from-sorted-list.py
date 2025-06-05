# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        head.next = self.deleteDuplicates(head.next)
        if head.next:
            next_node = head.next
            if next_node.val == head.val:
                head.next = next_node.next
        
        return head
        
