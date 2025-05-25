# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # in bit manipulation
        ans = 0
        for i in range(32):
            sm = 0
            for num in nums:
                if num < 0:
                    num &= (2**32-1)
                sm += (num >> i) & 1
            sm %= 3
            ans |= sm << i

       # chcking if it's signed 
        if ans >= (2**31):
            ans -= (2**32)
        return ans

        
        