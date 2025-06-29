# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7

        nums = [num for num in nums if num < target]
        nums.sort()
        n = len(nums)

        left, right = 0, n - 1
        res = 0

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                size = right - left 
                res = (res + pow(2, size, MOD)) % MOD
                left += 1
        return res