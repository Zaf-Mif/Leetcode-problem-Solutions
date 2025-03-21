# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        left ,  right = 0 , 0

        while right < len(s):
            right += 1
            ss = s[left:right+1]
            cntR = ss.count("R")
            cntL = ss.count("L")

            if cntL == cntR:
                cnt += 1
                left = right + 1

        return cnt - 1
