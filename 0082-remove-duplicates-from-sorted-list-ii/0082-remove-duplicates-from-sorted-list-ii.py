# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = ListNode(0, head)
        cur = head
        pre = res
        dup = -101
        while cur and cur.next:
            if cur.val == cur.next.val:
                dup = cur.val
            if cur.val == dup:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        if cur.val == dup:
            pre.next = None
        return res.next
