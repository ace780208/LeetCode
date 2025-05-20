# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs_max_depth(node):
            if not node:
                return 0
            left = dfs_max_depth(node.left)
            right = dfs_max_depth(node.right)
            return max(left, right) + 1
        
        level = dfs_max_depth(root)
        
        queue = deque([root])
        curr_lvl = 1
        ans = 0
        while queue:
            curr_node_count = len(queue)
            for _ in range(curr_node_count):
                curr = queue.popleft()
                if curr_lvl == level:
                    ans += curr.val
                    
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            curr_lvl += 1
        return ans
            
            
        