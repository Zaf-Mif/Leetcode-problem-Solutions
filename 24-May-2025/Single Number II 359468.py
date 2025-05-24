# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for c in nums:
            freq[c] += 1
        
        for key, value in freq.items():
            if value ==  1:
                return key 