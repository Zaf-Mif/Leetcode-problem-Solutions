# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left , right  =  0 , len(matrix)-1
        while left < right:

            for i in range(right - left):
                top , bottom = left , right 

                # save topleft 
                topLeft = matrix [top][left+i]

                # rotate bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left] 

                # rotate bottom right to bottom left 
                matrix[bottom - i][left] = matrix[bottom][right -i]  

                # rotate topright to bottom  right
                matrix[bottom ][right - i] = matrix[top+i][right]

                # rotate topleft to topright
                matrix[top+ i][right] = topLeft

            right -= 1
            left += 1
