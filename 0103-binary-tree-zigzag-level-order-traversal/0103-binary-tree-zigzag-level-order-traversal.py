# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root:
            queue = deque([root])
            leftstart = True
            while queue:
                nodes_curr_lv = len(queue)

                tmp_queue = deque([])
                for _ in range(nodes_curr_lv):

                    node = queue.popleft()
                    if leftstart:
                        tmp_queue.append(node.val)
                    else:
                        tmp_queue.appendleft(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                leftstart = not leftstart
                ans.append(list(tmp_queue))
        
        return ans