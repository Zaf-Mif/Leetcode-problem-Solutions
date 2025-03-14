# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.mx = 0
        def depth(node, cnt):
            if not node:
                self.mx = max(cnt , self.mx)
                return 
            depth(node.left , cnt + 1)
            depth(node.right, cnt + 1)

        depth(root,0)

        return self.mx
