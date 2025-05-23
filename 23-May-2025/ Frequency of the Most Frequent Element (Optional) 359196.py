# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # we can make an operation k times
        nums.sort()
        left, curr, ans = 0, 0, 0
        for right in range(len(nums)):
            target = nums[right]
            curr += target
            while ((right - left + 1) * target - curr) > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans

