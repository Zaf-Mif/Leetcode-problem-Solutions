# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurrence = [0]*26
        for i in range(len(s)):
            lastOccurrence[ord(s[i]) - ord("a")] = i
        
        start = end = 0
        size = []
        for i , char in enumerate(s):
            end = max(end , lastOccurrence[ord(char)-ord("a")])
            if i == end:
                size.append(i - start + 1)
                start = i + 1
        return size