# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        arrXor = 0
        for num in nums:
            arrXor ^= num
        
        # take the set bit 
        diff = 1 # 001 
        while not (arrXor & diff ):
            diff <<= 1
        
        # if there is set bit in that xor it with a else gn to b
        a, b = 0, 0
        for n in nums:
            if n & diff: # not equal to 0
                a ^= n
            else:
                b ^= n
        
        return [a,b]

