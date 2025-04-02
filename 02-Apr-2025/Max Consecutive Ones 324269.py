# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        cnt = 0

        for i in range(len(nums)):
            
            if nums[i] == 1 :
                cnt += 1
                mx = max(cnt , mx)
            else:
                cnt = 0

        return mx 