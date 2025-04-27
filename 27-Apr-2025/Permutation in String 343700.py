# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, k = len(s2), len(s1)
        
        if k > n:
            return False

        check = Counter(s1)
        window = Counter(s2[:k])

        if window == check:
            return True
            
        for right in range(k , n):
            window[s2[right]] += 1
            window[s2[right - k]] -= 1
            if window[s2[right - k]] == 0:
                del window[s2[right - k]]

            if window == check:
                return True

        return False