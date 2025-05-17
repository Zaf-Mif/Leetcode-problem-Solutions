class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nim = 0
        while nim < len(nums):
            for i in range(nim+1 , len(nums)):
                if nums[nim] > nums[i]:
                    nums[nim] , nums[i] = nums[i] , nums[nim]
            nim += 1

        

        