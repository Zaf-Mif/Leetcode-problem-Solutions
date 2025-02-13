# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = len(nums)-1
        k = k % len(nums)
        while left < right :
            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]