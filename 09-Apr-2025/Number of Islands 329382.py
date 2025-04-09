# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        ROWS , COLS = len(grid) , len(grid[0])
        directions = [(0,1) , (0 , -1) , (-1 , 0) , (1 , 0)]
            
        def dfs(row , col):
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or grid[row][col] == "0":
                return 

            grid[row][col] = "0"

            for dr , dc in directions:
                newr , newc = row + dr , col + dc
                dfs(newr , newc)
            
        for i in range(ROWS):
            for j in range (COLS):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i , j)
                    
        return island