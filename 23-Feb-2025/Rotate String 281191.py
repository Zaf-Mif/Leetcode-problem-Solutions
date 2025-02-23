# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        lst = [element for element in s ]
        for i in range(len(lst)):
            a = lst.pop(0)
            lst.append(a)
            ls = "".join(lst)
            if ls == goal:
                return True
        else:
            return False