# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd = sum([nums[i] for i in range(len(nums)) if i % 2 == 0])
        even = sum([nums[i] for i in range(len(nums)) if i % 2 != 0])
        cnt , left , right = 0 , 0 , 0
        for i in range(len(nums)):
            if i % 2 != 0:
                even -= nums[i] 
            else:
                odd -= nums[i]
            
            if left + even == right + odd:
                cnt += 1
            
            if i % 2 ==0 :
                left += nums[i]
            else:
                right += nums[i]

        return cnt


        