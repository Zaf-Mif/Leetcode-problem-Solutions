# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # ((nums[i] | nums[j]) & nums[k])
        arrXor = 0
        for num in nums:
            arrXor ^= num
        return arrXor