# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num = []
        for i in nums:
            num.append(int(i))
        print(num)
        num.sort()
        idx = len(nums) - k 
        return str(num[idx])