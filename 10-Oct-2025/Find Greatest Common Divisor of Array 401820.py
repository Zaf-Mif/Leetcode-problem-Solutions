# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a == 0: # or b ==0
                return b # or return a
            if a < b: # or a > b
                temp = a 
                a = b
                b = temp
            return gcd(a-b, b) # or gcd(a, b-a)
        mx = max(nums)
        mn = min(nums)

        return gcd(mx, mn)