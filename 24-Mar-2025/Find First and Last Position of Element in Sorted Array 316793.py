# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # upper bound search
        def rightSearch(target):
            low = 0 
            high = len(nums) -1
            right = -1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    right = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return right
            
        # lower bound search
        def leftSearch(target):
            low = 0 
            high = len(nums) -1
            left = -1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    left = mid
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                
            return left

        
        return [leftSearch(target) , rightSearch(target)]