# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # we asked to return the number of differce in bit 
        z = (x ^ y).bit_count()
        return z