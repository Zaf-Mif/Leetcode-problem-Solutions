# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        Rows, Cols = m , n
        dp = [[0] * (Cols+1) for i in range(Rows +1)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, Rows):
            for j in range(1, Cols):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[Rows-1][Cols-1]