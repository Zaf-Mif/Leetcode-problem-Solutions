# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        for i in nums:
            answer.append(answer[-1] * i)

        mult = 1 
        pre = [0] *len(nums)
        for i in range(len(nums)-1 , -1 , -1):
            pre[i] = answer[i] * mult
            mult *= nums[i]

        return pre