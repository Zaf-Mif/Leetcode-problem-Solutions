# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        hash = {}
        def dp(n):

            if n == 1 or n == 0:
                return n
            if n not in hash:
                hash[n] = dp(n-1) + dp(n-2)
            
            return hash[n]
            
        return dp(n)