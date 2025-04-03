# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            index = nums[i] - 1

            if index != i and nums[index] != nums[i]:
                nums[index] , nums[i] = nums[i] , nums[index]
            
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i]-1 != i :
                ans.append(i + 1)

        return ans
