# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = indices[:]
        for i in range((len(indices))):
            arr[indices[i]] = s[i]
        arr = "".join(arr)
        return arr
        