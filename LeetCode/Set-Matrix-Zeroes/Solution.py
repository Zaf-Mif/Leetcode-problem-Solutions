class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        COLS = len(matrix[0])
        ROWS = len(matrix)
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    for k in range(ROWS):
                        if matrix[k][col] == 0:
                            continue
                        matrix[k][col] = "0"
                    for z in range(COLS):
                        if matrix[row][z] == 0:
                            continue
                        matrix[row][z] = "0"
        

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == "0":
                    matrix[row][col] = 0




