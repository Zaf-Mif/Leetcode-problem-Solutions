# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or s[0] in "]})":
            return False
        stack = []
        for i in range(len(s)):
            if (s[i] == "(" or s[i] == "[" or s[i] == "{"):
                stack.append(s[i])
            else:
                if stack:
                    if not ((s[i] == ")" and stack[-1] == "(" ) or 
                            (s[i] == "]" and stack[-1] == "[") or 
                            (s[i] == "}" and stack[-1] == "{")):
                                return False
                    else:
                        stack.pop()
                else:
                    return False
        return True if not stack else False

