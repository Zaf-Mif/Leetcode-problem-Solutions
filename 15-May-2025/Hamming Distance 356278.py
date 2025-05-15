# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # we asked to return the number of differce in bit 
        z = (x ^ y)
        cnt = 0
        while z > 0:
            if (z & 1) != 0:
                cnt += 1
            z >>= 1
        return cnt 