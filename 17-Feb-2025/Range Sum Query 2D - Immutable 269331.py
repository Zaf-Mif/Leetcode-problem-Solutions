# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS , COLS = len(matrix) ,len(matrix[0])
        self.prefix = [[0] * (COLS +1) for i in range(ROWS+1)]
        for row in range(ROWS):
            for col in range(COLS):
                self.prefix[row+1][col+1] =  self.prefix[row][col+1] + self.prefix[row+1][col] + matrix[row][col] - self.prefix[row][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)