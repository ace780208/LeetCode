# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = ListNode(0, head)
        def recursive(head):
            if not head: 
                return True
            right = recursive(head.next)
            self.left = self.left.next
            return right and self.left.val == head.val
        return recursive(head)