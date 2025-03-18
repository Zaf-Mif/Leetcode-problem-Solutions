# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        buckets = defaultdict(list)

        for char, cnt in freq.items():
            buckets[cnt].append(char)
        
        ans = ""
        for i in range(len(s) , 0 , -1):
            for j in buckets[i]:
                ans += (j * i)

        return ans
            