# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        res = []
        # for row in range(len(mat)):
        #     for col in range(len(mat[0])):
        ROWS = len(mat)
        COLS = len(mat[0])
        row , col , direction  = 0 , 0, 1
        upright = 1
        for i in range(ROWS * COLS):
            #for upright
            if upright == 1:
                if col == COLS -1:
                    res.append(mat[row][col])
                    row += 1
                    upright = -1
                elif row == 0:
                    res.append(mat[row][col])
                    col += 1
                    upright = -1
                else:
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
            # for downleft 
            else:
                if row == ROWS-1:
                    res.append(mat[row][col])
                    col += 1
                    upright = 1
                elif col == 0:
                    res.append(mat[row][col])
                    row += 1
                    upright = 1
                else:
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
        return res