# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 
        stac = []
        curr = root

        while curr or stac:
            while curr:
                stac.append(curr)
                curr = curr.left

            curr = stac.pop()
            n += 1
            if n == k:
                return curr.val

            curr =  curr.right