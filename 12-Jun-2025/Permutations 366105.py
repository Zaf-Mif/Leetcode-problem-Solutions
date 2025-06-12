# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        def backtrack(num):
            if len(path) == n:
                ans.append(path.copy())
                return
            
            for i in range(n):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(nums[i])
                    path.pop()


        backtrack(0)
        return ans

        