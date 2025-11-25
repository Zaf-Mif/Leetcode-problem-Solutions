# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # by using cyclic sort 
        i = 0
        n = len(nums)
        
        while i < n :
            index = nums[i]
            if nums[i] == n:
                i += 1
            elif index != i:
                nums[index] , nums[i] = nums[i] , nums[index]
            else: 
                i += 1

        # checking which one is missing
        for i in range(n):
            if nums[i] != i:
                return i
        else:
            return n
        
            