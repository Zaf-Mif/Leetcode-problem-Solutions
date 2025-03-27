# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = float("inf")
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= nums[high]:
                low = mid + 1
            else:
                ans = min(ans , nums[mid])
                high = mid - 1

        return min(ans,nums[mid])