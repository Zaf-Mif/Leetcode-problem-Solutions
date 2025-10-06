# Problem: Remove Duplicates from Sorted Array
(Easy) - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = defaultdict (int)
        for c in nums:
            freq[c] += 1

        unq = list(freq.keys())
        for i in range(len(unq)):
            nums[i] = unq[i]
        
        return len(unq)
