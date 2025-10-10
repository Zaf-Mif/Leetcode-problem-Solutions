# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        no = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                no += 1
        return no