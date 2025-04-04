# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def largest(node, level):
            if not node :
                return 
            
            if level == len(res):
                res.append(node.val)
            else:
                res[level] = max(node.val , res[level])
            

            largest(node.left , level + 1)
            largest(node.right , level + 1)

        largest(root , 0)
        return res