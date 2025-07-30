# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution: def isValid(self, s: str) -> bool: stack=[] for i in s: if i is "[" or i== "(" or i=="{": stack.append(i) else: if not stack or not ((stack[-1] == "[" and i =="]") or (stack[-1] == "(" and i ==")") or (stack[-1] == "{" and i =="}")): return False stack.pop() return not stack