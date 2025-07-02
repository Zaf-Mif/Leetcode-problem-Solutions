# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, qs: List[str], p: str) -> List[bool]:
        def v(s):
            return [a for a in s if a.isupper()]

        def IsUp(s, t):
            it = iter(t)
            return all(a in it for a in s)
        return [v(p) == v(q) and IsUp(p, q) for q in qs]