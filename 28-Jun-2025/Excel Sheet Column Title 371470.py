# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber > 0:
            columnNumber -= 1

            s += chr(ord('A') + (columnNumber) % 26)

            columnNumber //= 26

        return s[::-1]