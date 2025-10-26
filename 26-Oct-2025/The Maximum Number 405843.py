# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = set(nums)
        if len(n) < 3:
            return max(n)
        
        first= second= third = float("-inf")
        for i in n:
            if i >= first:
                temp = second
                second = first
                first = i
                third = temp

            elif i < first and i >= second:
                third = second
                second = i

            elif i < first and i < second and i >= third:
                third = i
             
        return third