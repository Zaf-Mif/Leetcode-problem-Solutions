# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a == 0:
                return b
            if a < b:
                a, b = b, a
            return gcd(a-b , b)
        mx = max(nums)
        mn = min(nums)

        return gcd(mx, mn)