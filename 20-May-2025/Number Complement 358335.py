# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        # toggling 
        # getting the length and
        # 1 << length -1
        # mask ^ num
        length = num.bit_length()
        mask = (1 << length) -1
        return num ^ mask
