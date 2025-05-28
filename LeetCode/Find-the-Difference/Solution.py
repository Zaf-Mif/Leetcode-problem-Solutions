class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arrXor = 0
        for word in s:
            arrXor ^= ord(word)
        for word in t:
            arrXor ^= ord(word)
        return chr(arrXor)