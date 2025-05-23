# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node, curr):
            if not node:
                 return curr

            curr_dist = abs(target - curr)
            node_dist = abs(target - node.val)
            if node_dist < curr_dist:
                curr = node.val
            elif curr_dist == node_dist:
                curr = min(curr, node.val)

            if target < node.val:
                return dfs(node.left, curr)
            else:
                return dfs(node.right, curr)

        return dfs(root, float("inf"))