# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums and len(nums)< 3:
            return 0
        nums.sort()

        mx = float("inf")
        for i in range(len(nums)-2):
            left , right  = i+1 , len(nums) - 1
            while left < right:
                sm = nums[i] + nums[left] + nums[right]
                if abs(sm-target) < abs(mx-target):
                    mx = sm
                elif sm < target:
                    left += 1
                else:
                    right -= 1
        return mx