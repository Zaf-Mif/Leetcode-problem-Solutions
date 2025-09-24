# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def reverse_fibonacci(m):
            if m == 0 or m ==1:
                return 1

            if m in memo:
                return memo[m] 
            memo[m] = reverse_fibonacci(m-1) + reverse_fibonacci(m-2)

            return memo[m]

        return reverse_fibonacci(n)