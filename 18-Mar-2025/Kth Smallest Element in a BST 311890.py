# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.ans = None

        def inorder(node):
            if node is None or self.ans is not None:
                return

            inorder(node.left)

            self.cnt += 1

            if self.cnt == k:
                self.ans = node.val
                return 

            inorder(node.right)

        inorder(root)
        return self.ans
                    


            