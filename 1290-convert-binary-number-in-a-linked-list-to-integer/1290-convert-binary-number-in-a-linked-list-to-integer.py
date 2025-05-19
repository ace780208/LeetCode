# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        dummy = head
        ans = 0 
        while dummy:
            ans = (ans << 1) + dummy.val
            dummy = dummy.next
        return ans