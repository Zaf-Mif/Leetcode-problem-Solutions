# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # by using bucket sort
        def merge(left_half , right_half):
            left = 0 
            right = 0
            merged = []

            while left < len(left_half) and right < len(right_half):
                if left_half[left] <= right_half[right]:
                    merged.append(left_half[left])
                    left += 1
                else:
                    merged.append(right_half[right])
                    right += 1
            
            while left < len(left_half):
                merged.append(left_half[left])
                left += 1
                
            while right < len(right_half):
                merged.append(right_half[right])
                right += 1
    
            return merged
        
        def mergeSort(left , right , arr):
            if left == right :
                return [arr[left]]
            
            mid = left +( right - left )// 2

            left_half = mergeSort(left , mid , arr )
            right_half = mergeSort(mid + 1 , right , arr)

            return merge(left_half , right_half)

        return mergeSort(0 , len(nums)-1 , nums)