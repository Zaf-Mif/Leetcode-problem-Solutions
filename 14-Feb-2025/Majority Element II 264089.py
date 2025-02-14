# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = 0
        for i in nums:
            if count == 0:
                res = i
            
            if count == (len(nums)//3):
                count += 1
            else:
                count -= 1
        return res