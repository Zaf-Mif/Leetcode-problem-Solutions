# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # getting the bit as a string and iterate through it to get the d/t bit and return False then True
        cnt = bin(n)[2:]
        # print(cnt)
        for i in range(len(cnt)-1):
            if cnt[i] == cnt[i+1]:
                return False
        return True