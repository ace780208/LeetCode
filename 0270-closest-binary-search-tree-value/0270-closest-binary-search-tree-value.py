# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.curr_min = root.val
        def dfs(node):
            if not node:
                return
            
            self.curr_min = min(self.curr_min, node.val, key=lambda x: (abs(target - x), x))

            if target > node.val:
                dfs(node.right)
            else:
                dfs(node.left)
        dfs(root)
        return self.curr_min 