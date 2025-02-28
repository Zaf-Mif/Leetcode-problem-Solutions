# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = defaultdict(int)
        for c in nums:
            single[c] += 1
        for key , value in single.items():
            if value == 1:
                return key 