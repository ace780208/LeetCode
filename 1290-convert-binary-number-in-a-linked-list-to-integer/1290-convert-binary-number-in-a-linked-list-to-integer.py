# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        dummy = head
        ans = []
        while dummy:
            ans.append(str(dummy.val))
            dummy = dummy.next
        return int(''.join(ans), 2)