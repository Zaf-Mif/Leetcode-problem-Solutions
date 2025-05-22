# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 0 
        current = 0 # bitmask
        left = 0

        for right in range(len(nums)):
            while current & nums[right]:
                current = current ^ nums[left] # unsset
                left += 1

            result = max(result , right - left + 1)  
            current = current | nums[right]

        return result
