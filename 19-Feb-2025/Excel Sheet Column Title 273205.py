# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber > 0:
                
            Nu = (columnNumber - 1) % 26
            s += chr(ord('A') + Nu)

            columnNumber = (columnNumber - 1) // 26

        return s[::-1]