# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the number of total nodes
        total = 0
        dummy = head
        while dummy:
            total += 1
            dummy = dummy.next

        # remove the nth node from the end
        removed_nth = total - n
        dummy = head
        order = 0
        prev = None
        while dummy:
            if order == removed_nth:
                if prev:
                    prev.next = dummy.next
                else:
                    head = dummy.next
                break
            order += 1
            prev = dummy
            dummy = dummy.next
        return head