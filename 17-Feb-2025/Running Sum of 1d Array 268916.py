# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        sm = 0
        for i in nums:
            sm += i
            running_sum.append(sm)
        return running_sum