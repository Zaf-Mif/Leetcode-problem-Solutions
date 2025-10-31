# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)
        for c in nums:
            hash[c] += 1
        ans = []
        for key, value in hash.items():
            if value == 2:
                ans.append(key)
        return ans