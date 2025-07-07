# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = defaultdict(int)
        ans = []
        for i in nums:
            res[i] += 1
        
        for key,value in res.items():
            if value == 2:
                ans.append(key)
        return ans