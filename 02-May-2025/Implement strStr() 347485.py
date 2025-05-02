# Problem: Implement strStr() - https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            print(-1)
        n= len(needle)
        s=0
            
        while n<=len(haystack):
            if needle == haystack [s:n]:
                return s
            else:
                s+=1
                n+=1
        return -1