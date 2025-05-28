# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        freq = defaultdict(int)
        for c in nums:
            freq[c] += 1

        for key, value in freq.items():
            if value == 1:
                res.append(key)
        return res