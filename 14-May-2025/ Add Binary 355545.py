# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # change to decimal then add  then to binary 
        return(bin(int(a,2) + int(b,2))[2:])
        # return int(a) ^ int(b)
