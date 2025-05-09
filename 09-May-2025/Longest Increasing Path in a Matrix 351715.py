# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        @cache
        def dfs(row,col):
            res = 1
            def inbound(r,c):
                return 0<=r<n and 0<=c<m
            
            for dx,dy in directions:
                dx = row + dx
                dy = col + dy
                if inbound(dx,dy) and (matrix[row][col] < matrix[dx][dy]) :
                    res = max(res, 1 + dfs(dx,dy)) # +1 is for ur self
            return res

        ans = 1
        n , m = len(matrix) ,len(matrix[0])
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i,j))
        
        return ans