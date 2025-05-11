# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre = max_pre = 0
        pre  = 0 
        for num in nums:
            pre += num
            min_pre = min(min_pre , pre)
            max_pre = max(max_pre, pre)

        return max_pre - min_pre

