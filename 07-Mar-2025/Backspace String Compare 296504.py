# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackc = []
        stackt = []
        for i in range(len(s)):
            if s[i] == "#" :
                if stackc:
                    stackc.pop()
            else:
                stackc.append(s[i])
        for i in range(len(t)):
            if t[i] == "#":
                if stackt:
                    stackt.pop() 
            else:
                stackt.append(t[i])  

        return stackc == stackt
