# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree curr.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root):
            if not root:
                return []
                
            queue = deque([root])
            res = []

            while queue:
                temp = []
                # res.append(curr.val for curr in queue )

                for _ in range(len(queue)):
                    curr = queue.popleft()
                    temp.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)

                    if curr.right:
                        queue.append(curr.right)
                    
                res.append(list(temp))
            return res

        return dfs(root)