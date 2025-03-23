# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i , arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return 
            
            for j in range(len(nums)):
                if nums[j] not in arr:
                    arr.append(nums[j])
                    backtrack(j+1 , arr)
                    arr.pop()
            

        backtrack(0,[])
        return res

        