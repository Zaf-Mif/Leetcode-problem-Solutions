# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        val = 0
        for i in range(2,n+1):
            val = (val+k) % i
        return val + 1