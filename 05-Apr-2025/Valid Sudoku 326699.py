# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(mat):
            ROWS = 9
            
            # to check if the row is valid
            def checkRow(mat):
                for row in mat:
                    n = set()
                    for num in row:
                        if num != "." :
                            if  num in n:
                                return False
                            n.add(num)
                return True
            
            # to check if the column is valid
            def checkCols(mat):
                for col in range(ROWS):
                    n = set()
                    for row in range(ROWS):
                        num = (mat[row][col])
                        if num != "." :
                            if  num in n:
                                return False
                            n.add(num)
                return True
            
            # to check the 3 * 3 matrix
            def subgrid(mat):
                for row in range(0 ,ROWS, 3):
                    for col in range(0, ROWS, 3):
                        n = set()
                        
                        for i in range(3):
                            for j in range(3):
                                num = (mat[row + i][col+j])
                                if num != "." :
                                    if  num in n:
                                        return False
                                    n.add(num)
                return True
                        

            return (checkRow(mat) and checkCols(mat) and subgrid(mat)) 

        return check(board)