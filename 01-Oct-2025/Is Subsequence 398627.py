# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        Rows = len(s)
        Cols = len(t)

        dp = [[False] * (Cols + 1) for _ in range(Rows + 1)]

        for j in range(Cols+1):
            dp[0][j] = True

        for i in range(1,Rows+1):
            for j in range(1, Cols+1):
                if s[i-1] in t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        print(dp)
        return dp[Rows][Cols]