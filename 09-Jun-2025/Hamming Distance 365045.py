# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # we asked to return the number of differce in bit 
        z = (x ^ y)
        cnt = 0
        for i in range(32):
            if (z & (1 << i)) != 0:
                cnt += 1
            # z >>= 1
        return cnt 