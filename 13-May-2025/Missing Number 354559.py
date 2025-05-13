# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Bit Manipulation
        #  xor x^y^y = x
        n = len(nums)
        rangeXor = 0 
        arrXor = 0

        for i in range(n+1):
            rangeXor ^= i
        
        for num in nums:
            arrXor ^= num
        
        return arrXor ^ rangeXor