# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_max, curr_min):
            if not node:
                return curr_max - curr_min
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            left_diff = dfs(node.left, curr_max, curr_min)
            right_diff = dfs(node.right, curr_max, curr_min)
            return max(left_diff, right_diff)
        
        return dfs(root, float("-Inf"), float("Inf"))