class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ans = []
        COLS = len(matrix[0])
        ROWS = len(matrix)
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    ans.append([row,col])
        
        for r,c in ans:
            for k in range(ROWS):
                matrix[k][c] = 0
            for z in range(COLS):
                matrix[r][z] = 0

