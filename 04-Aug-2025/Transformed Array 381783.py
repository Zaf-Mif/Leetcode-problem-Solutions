# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        for i, x in enumerate(nums):
            result[i] = nums[(i + x) % n]
        return result