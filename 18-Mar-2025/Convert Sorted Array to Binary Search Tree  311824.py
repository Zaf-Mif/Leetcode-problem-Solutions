# Problem: Convert Sorted Array to Binary Search Tree  - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def solve(left , right):
            if (right - left + 1) == 0:
                return None
                
            if (right - left + 1) == 1:
                return TreeNode(nums[left])

            mid = (right + left ) // 2

            root = TreeNode(nums[mid])

            root.left = solve(left , mid-1)
            root.right = solve(mid+1 , right)

            return root 

        return solve (0, len(nums)-1)
