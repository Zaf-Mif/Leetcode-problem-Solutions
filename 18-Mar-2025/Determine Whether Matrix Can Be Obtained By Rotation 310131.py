# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):

            left , right  =  0 , len(mat)-1
            while left < right:

                for i in range(right - left):
                    top , bottom = left , right 

                    # save topleft 
                    topLeft = mat [top][left+i]

                    # rotate bottom left to top left
                    mat[top][left + i] = mat[bottom - i][left] 

                    # rotate bottom right to bottom left 
                    mat[bottom - i][left] = mat[bottom][right -i]  

                    # rotate topright to bottom  right
                    mat[bottom ][right - i] = mat[top+i][right]

                    # rotate topleft to topright
                    mat[top+ i][right] = topLeft

                right -= 1
                left += 1


            if mat == target :
                return True
            
        return False

                
                