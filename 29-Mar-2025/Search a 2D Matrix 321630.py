# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row , col = len(matrix) , len(matrix[0])
        low = 0
        high = (row * col) - 1

        while low <= high :
            mid = low + (high - low ) // 2
            check = matrix[mid // col][mid % col]

            if check == target:
                return True
            elif check > target :
                high = mid - 1
            else:
                low = mid + 1
        return False
        
