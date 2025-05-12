# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get the first and sec half of linked list through fast and slow pointers
        sec = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = sec
            sec = sec.next
            fast = fast.next.next

        if prev:
            prev.next = None
        else:
            return True

        # reverse the linked list
        reversed_nodes = self.reverse(sec)

        # loop through both origin and the reverse linked list has the same val
        dummy = head
        while dummy:
            first = dummy.val
            second = reversed_nodes.val
            if first != second:
                return False
            dummy = dummy.next
            reversed_nodes = reversed_nodes.next

        return True

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
    
