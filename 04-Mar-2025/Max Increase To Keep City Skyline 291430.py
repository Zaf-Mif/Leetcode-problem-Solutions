# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        max_row = []
        for row in range(ROWS):
            r = max(grid[row])
            max_row.append(r) 

        max_col = []
        for c in range(COLS):
            temp = []
            for r in range(ROWS):
                temp.append(grid[r][c])
            max_col.append(max(temp))

        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                skyline = min(max_row[row], max_col[col])
                result += (skyline - grid[row][col])

        return result
