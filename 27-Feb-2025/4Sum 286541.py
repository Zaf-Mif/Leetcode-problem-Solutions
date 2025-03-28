# Problem: 4Sum - https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans  = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1 , len(nums)-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left , right = j+1 , len(nums)-1

                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        ans.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif nums[i] + nums[j] + nums[left] + nums[right] > target :
                        right -= 1
                    else:
                        left += 1
        return ans