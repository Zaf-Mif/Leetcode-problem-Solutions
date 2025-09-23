# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        n1, n2  = len(v1), len(v2)
        for x1, x2  in zip(v1,v2):
            if int(x1) < int(x2):
                return -1
            if int(x1) > int(x2):
                return 1
        n3 = min(n1, n2)
        if n1 < n2:
            return -1 if any(int(v2[i]) > 0 for i in range(n3, n2)) else 0
        if n1 > n2:
            return 1 if any(int(v1[i]) > 0 for i in range(n3, n1)) else 0
    
        return 0 
            



