# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = sm = 0
        right = int(sqrt(c))
        while left <= right:
            sm = ((left*left) + (right*right))
            if sm == c:
                return True
            elif sm < c:
                left += 1
            else:
                right -= 1
            
        return False