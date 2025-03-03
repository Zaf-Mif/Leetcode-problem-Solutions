# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        mx = 0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                mx = max(mx , (nums[i]+ nums[i+1] + nums[i+2]))
        return mx