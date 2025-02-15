# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        cnt,left_over = 0, len(nums)
        left , right = 0 , 1
        while right < len(nums) :
            if nums[left] == nums[right]:
                left_over -= 2
                cnt += 1
                left += 2
                right += 2
            else:
                left += 1
                right += 1
        return [cnt , left_over]
