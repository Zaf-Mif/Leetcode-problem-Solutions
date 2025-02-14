# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even = sum([num for num in nums if num % 2 == 0])
        odd = sum([num for num in nums if num % 2 == 1] )
        for i in range(len(queries)):
            index = queries[i][1]
            value = queries[i][0]

            # updating our even and odd
            if nums[index] % 2 == 0:
                even -= nums[index]
            else:
                odd -= nums[index]
            
            nums[index] += value
            # updating our value of even and odd after updating nums
            if nums[index] % 2== 0:
                even += nums[index]
            else:
                odd += nums[index]

            result.append(even)
        return result