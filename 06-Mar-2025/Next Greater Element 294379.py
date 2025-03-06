# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = defaultdict(lambda : -1)
        monotonic_decrease = []
        for num in nums2:
            while monotonic_decrease and monotonic_decrease[-1] < num:
                value = monotonic_decrease.pop()
                ans[value] = num
            monotonic_decrease.append(num)

        return [ans[num] for num in nums1]
