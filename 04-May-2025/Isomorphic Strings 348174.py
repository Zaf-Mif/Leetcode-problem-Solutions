# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()

        for c1, c2 in zip(s, t):
            if c1 in mapping:
                if mapping[c1] != c2:
                    return False
            else:
                if c2 in used:
                    return False
                mapping[c1] = c2
                used.add(c2)
                
        return True