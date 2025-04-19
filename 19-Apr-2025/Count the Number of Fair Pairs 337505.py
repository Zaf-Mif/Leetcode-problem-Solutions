# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        count = 0

        for i in range(n):
            left = bisect.bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect.bisect_right(nums, upper - nums[i], i + 1, n)
            count += (right - left)

        return count