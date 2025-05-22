# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        left2right = True
        output = []
        while queue:
            node_count = len(queue)
            level_vals = deque()
            for _ in range(node_count):
                node = queue.popleft()
                if left2right:
                    #print(node.val)
                    level_vals.append(node.val)
                else:
                    #print(node.val)
                    level_vals.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(list(level_vals))
            left2right = not left2right
        
        return output