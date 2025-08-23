# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        res = [-1] * (len(nums) - k + 1)
        while r < len(nums):
            if r > 0 and nums[r - 1] + 1 != nums[r]:
                l = r
            if r - l + 1 >= k:
                res[r - (k - 1)] = nums[r]
            r += 1

        return res