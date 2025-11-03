# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        def dfs(node, small, large):
            if not node:
                return
            
            if node.val > target:
                large = min(node.val, large)
                dfs(node.left, small, large)
            
            if node.val < target:
                small = max(node.val, small)
                dfs(node.right, small, large)
            
            nonlocal ans
            ans_diff = abs(ans - target)
            cur_diff = abs(node.val - target)
            if ans_diff > cur_diff:
                ans = node.val
            elif ans_diff == cur_diff:
                ans = min(ans, node.val)
        
        dfs(root, float("-Inf"), float("Inf"))
        return ans
            