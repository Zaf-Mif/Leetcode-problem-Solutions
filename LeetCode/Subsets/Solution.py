class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i , arr):
            # if len(arr) > len(nums):
            #     return 

            ans.append(arr[::])

            for j in range(i, len(nums)):
                arr.append(nums[j])

                backtrack(j+1 , arr)
                arr.pop()

        backtrack(0,[])

        return ans
