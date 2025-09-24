# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(m):
            if m == 2 or m == 1:
                return m

            return dp(m-1) + dp(m-2)

        return dp(n)