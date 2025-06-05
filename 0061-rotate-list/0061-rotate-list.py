# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        end = None
        # count the total nodes
        counts = 0
        while curr:
            counts += 1
            if not curr.next:
                end = curr
            curr = curr.next
        #print(counts)
        # reduce the rotate time if needed
        if k >= counts:
            k %= counts

        # get to the prev and node to move
        curr = head
        #print(k)
        if k > 0:
            while k > 0:
                curr = curr.next
                k -= 1
            
            while curr:
                prev = prev.next
                curr = curr.next
            
            # change pointer
            new_start = prev.next
            prev.next = None
            end.next = head
            dummy.next = new_start

        return dummy.next

