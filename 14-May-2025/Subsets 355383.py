# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        m = 2 ** n
        ans = []
        
        for num in range(m):
            temp = []
            for i in range(32):
                if num & (1<<i) != 0: #it means 1
                    temp.append(nums[i])

            ans.append(temp)

        return ans
