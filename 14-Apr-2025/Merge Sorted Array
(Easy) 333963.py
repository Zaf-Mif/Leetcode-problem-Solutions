# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = 0
        i = 0
        temp = nums1[left]
        while left < len(nums1) and right <len(nums2):
            if nums1 and nums2 :

                if nums1[left] < nums2[right]:

                    if nums1[left] == 0:
                        nums1[i] = nums2[right]
                        right += 1
                        left += 1
                    else:
                        nums1[i] = nums1[left]
                        left += 1

                else:
                    if nums2[right] == 0:
                        nums1[i] = nums1[left]
                        left += 1
                        right += 1
                    else:
                        nums1[i] = nums2[right]
                        right += 1

            i += 1
            
            # if nums1 and not nums2:

                