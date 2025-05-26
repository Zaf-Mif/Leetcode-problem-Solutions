# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for c in nums:
            freq[c] += 1
        
        for key, value in freq.items():
            if value != 1:
                return key
    