# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height)-1
        res = 0
        while left < right:
            res =max((min(height[left] , height[right])) *(right - left ), res)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res