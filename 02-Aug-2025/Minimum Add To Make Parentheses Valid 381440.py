# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # abs(opening - closing)

        opening , closing = 0 , 0 
        for i in range(len(s)):
            if s[i] == "(":
                opening += 1
            elif s[i] == ")":
                if opening == 0:
                    closing += 1
                else:
                    opening -= 1

        return closing + opening