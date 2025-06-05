# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr and curr.next:
            #print(f"before {curr.val}, {curr.next.val}")
            next_stop = curr.next.next
            curr.next.next = curr
            prev.next = curr.next
            curr.next = next_stop
            prev = curr
            curr = next_stop
            #print(f"after {curr.val}, {curr.next.val}")
        return dummy.next

