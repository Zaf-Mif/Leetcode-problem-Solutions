# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_so_far, max_so_far):
            if not node:
                return max_so_far - min_so_far
            
            min_so_far = min(min_so_far, node.val)
            max_so_far = max(max_so_far, node.val)
            
            left = dfs(node.left, min_so_far, max_so_far)
            right = dfs(node.right, min_so_far, max_so_far)
            
            return max(left, right)
        
        return dfs(root, root.val, root.val)