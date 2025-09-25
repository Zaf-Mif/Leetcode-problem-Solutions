# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        @cache
        def dp(i, j):
            if i == n1 or j == n2:
                return 0
            take = not_take1 = not_take2 = 0
            # take
            if text1[i] == text2[j]:
                take = 1+ dp(i+1, j+1)
            #  not_take
            else:
                not_take1 = dp(i, j+1)
                not_take2 = dp(i+1, j)
            
            return max(take, not_take1, not_take2)
        return dp(0,0)