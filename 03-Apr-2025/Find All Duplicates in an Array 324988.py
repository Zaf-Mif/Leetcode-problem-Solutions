# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        ans = set()
        while i < len(nums):
            index = nums[i] - 1

            if index != i:
                if nums[index] == nums[i]:
                    ans.add(nums[i])
                    i += 1
                else:
                    nums[index] , nums[i] = nums[i] , nums[index]
            
            else:
                i += 1
        return list(ans)