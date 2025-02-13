# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left , right):
            while left < right :
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1
                right -= 1

        k = k % len(nums)
        # calling the function to reverse the whole array
        reverse(0,len(nums)-1)
        # calling the function to reverse the array from 0 to k
        reverse(0,k-1)
        #calling the function to reverse the remaining array
        reverse(k,len(nums)-1)