# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i , num in enumerate(nums):
            nums[i] = str(num)

        def check(l1,l2):
            if l1 + l2 > l2 + l1:
                return -1
            else :
                return 1
        
        nums = sorted(nums, key = cmp_to_key(check))

        return str(int("".join(nums)))
