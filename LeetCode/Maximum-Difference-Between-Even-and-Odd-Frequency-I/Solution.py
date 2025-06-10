class Solution:
    def maxDifference(self, s: str) -> int:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        even , odd = [] , []
        for key, value in freq.items():
            if value % 2 == 0:
                even.append(value)
            else:
                odd.append(value)
            
        mx = max(odd)
        mn = min(even)

        return mx - mn