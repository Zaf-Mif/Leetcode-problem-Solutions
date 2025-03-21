# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        memorization = {}
        def reverse_fibonacci(i):
            # if i == n or i == n-1:
            #     return 1
            
            if i == 0 or i ==1:
                return 1

            if i in memorization:
                return memorization[i]

            memorization[i] =  reverse_fibonacci(i-1) + reverse_fibonacci(i-2)
        
            return memorization[i]

        ans = reverse_fibonacci(n)
        return ans