# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        dup = 0
        while i < len(nums):
            index = nums[i] - 1

            if index != i:
                if nums[index] == nums[i]:
                    dup = nums[i]
                    i += 1
                else:
                    nums[index] , nums[i] = nums[i] , nums[index]
            
            else:
                i += 1
        
        rem = 0
        for i in range(len(nums)):
            if nums[i]-1 != i :
                rem = i + 1
        
        return [dup , rem]
        