# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # we can make an operation k times
        nums.sort()
        left, curr = 0, 0
        for right in range(len(nums)):
            target = nums[right]
            curr += target
            if (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
        return len(nums) - left

