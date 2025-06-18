class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(1, len(nums)-1, 3):
            if nums[i+1] - nums[i-1] > k:
                return []
            if (nums[i] - nums[i-1] <= k and 
                nums[i+1] - nums[i] <= k and 
                nums[i+1] - nums[i-1]<= k):
                    ans.append([nums[i-1], nums[i], nums[i+1]])
        
        return ans