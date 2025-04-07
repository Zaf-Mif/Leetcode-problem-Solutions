# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS , COLS = len(grid) , len(grid[0])
        perimeter = 0
     
        def dfs(row , col):
            
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or grid[row][col] == 0:
                return 1

            if grid[row][col] == -1:
                return 0

            grid[row][col] = -1
#[(0,1) , (0 , -1) , (-1 , 0) , (1 , 0)]
            return dfs(row , col + 1) + dfs(row , col -1) + dfs(row-1, col) + dfs(row + 1 , col)
 
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    # dfs(row, col)
                    perimeter += dfs(row, col)
        return perimeter