# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n , m = len(word1), len(word2)
        mn = min(n,m)

        s = ''
        for i in range(mn):
            s += word1[i]
            s += word2[i]
        if mn < n:
            s += word1[mn:]
        if mn < m:
            s += word2[mn:]
        
        return s