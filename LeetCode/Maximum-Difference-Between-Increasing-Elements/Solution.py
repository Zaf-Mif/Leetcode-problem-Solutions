class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # they don't have to be consecutive
        mx = float("-inf")
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    mx = max(mx, nums[j] - nums[i])

        return mx if mx != float("-inf") else -1
