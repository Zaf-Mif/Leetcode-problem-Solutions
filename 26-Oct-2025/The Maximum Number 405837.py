# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return (sorted(set(nums)))[-3] if len(set(nums)) >= 3 else max(nums)