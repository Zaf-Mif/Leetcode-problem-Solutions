# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution: def singleNumber(self, nums: List[int]) -> int: cnt = Counter(nums) # {2:2,1:!} for i, j in cnt.items(): if j == 1: return i 