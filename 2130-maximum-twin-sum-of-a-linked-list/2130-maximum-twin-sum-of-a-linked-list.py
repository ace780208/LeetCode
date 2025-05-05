# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # get the second half of the linked list with slow pointer
        fast = head
        slow = head
        n = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            n += 1
        
        # reverse the second half of the second half of linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # get the max of twin sum
        i = 0
        ans = 0
        dummy = head
        while i < n:
            twin_sum = dummy.val + prev.val
            ans = max(ans, twin_sum)
            dummy = dummy.next
            prev = prev.next
            i += 1

        return ans
