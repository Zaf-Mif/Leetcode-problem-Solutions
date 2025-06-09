# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = (start ^ goal)
        cnt = 0
        while num > 0:
            if (num & 1) != 0:
                cnt += 1
            num >>= 1
        return cnt