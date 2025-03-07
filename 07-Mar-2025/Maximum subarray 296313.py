# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        sm = 0

        for i in nums:
            if sm < 0:
                sm = 0
            sm += i
            mx = max(mx, sm)
        
        return mx