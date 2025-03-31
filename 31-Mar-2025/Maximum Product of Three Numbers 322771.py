# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pos = nums[-1] * nums[-2] * nums[-3]
        neg = nums[0] * nums[1] * nums[2]
        mid = nums[0] * nums[1] * nums[-1]
        return max(neg , pos , mid)
        