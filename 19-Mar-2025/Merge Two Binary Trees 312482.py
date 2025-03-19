# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def inside(left, right):
            if left is None and right is None:
                return None
            elif left is None:
                return right
            elif right is None:
                return left
            
            node = TreeNode(left.val + right.val)
            node.left = inside(left.left, right.left)
            node.right = inside(left.right, right.right)

            return node

        return inside(root1, root2)