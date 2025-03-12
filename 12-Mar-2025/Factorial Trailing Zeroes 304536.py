# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def trialing(n):
            if n < 5:
                return 0         
            n = n // 5
            return n + trialing(n)

        return trialing(n)
    