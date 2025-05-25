# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # in bit manipulation
        arrXor = [0]*32
        for num in nums:
            for i in range(32):
                if num & (1<<i) != 0:
                    arrXor[i] += 1

        ans = 0
        for i in range(32):
            if arrXor[i] % 3 != 0:
                ans |= (1<<i)

        # chcking if it's signed 
        if ans >= (1<<31):
            ans -= (1<<32)
        return ans

        
        