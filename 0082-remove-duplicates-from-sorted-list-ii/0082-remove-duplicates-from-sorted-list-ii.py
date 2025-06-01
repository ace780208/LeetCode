# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        prev, cur = dummy_head, head
        
        while cur and cur.next:
            if cur.val != cur.next.val:
                # If there's no duplicate,
                # move prev and cur one step forward
                prev, cur = cur, cur.next
            else:
                # If there're duplicates,
                # iterate cur to the last duplicate nodes,
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                    
                # and jump over the duplicates
                prev.next = cur.next
                cur = cur.next
        
        return dummy_head.next