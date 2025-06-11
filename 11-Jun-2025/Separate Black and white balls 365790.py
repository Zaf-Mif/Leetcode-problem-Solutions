# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        white = 0
        total = 0
        for curr, char in enumerate(s):
            if char == "0":
                total += curr - white

                white += 1

        return total