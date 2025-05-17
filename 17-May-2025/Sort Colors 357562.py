# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # can i just use 
        num = 0
        while num < len(nums):
            for i in range(num + 1, len(nums)):
                if nums[num] > nums[i]:
                    nums[num], nums[i] = nums[i], nums[num]
            num += 1
        