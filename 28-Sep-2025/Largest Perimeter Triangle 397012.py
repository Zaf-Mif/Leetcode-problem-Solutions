# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largest = 0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i+2] < nums[i+1] + nums[i]:
                peri = nums[i] + nums[i+1] +nums[i+2]
                largest = max(largest, peri)
        return largest 
