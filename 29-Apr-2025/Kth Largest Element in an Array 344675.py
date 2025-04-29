# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap =[]
        for num in nums:
            heappush(heap , -num)
        
        while k > 1:
            val = -heappop(heap)
            k -= 1
        
        return - 1 * heap[0]