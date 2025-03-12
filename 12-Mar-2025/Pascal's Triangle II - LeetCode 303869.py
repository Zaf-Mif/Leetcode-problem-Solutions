# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        prev_row = self.getRow(rowIndex-1)
        current_row = [1]

        for i in range(len(prev_row) -1):
            current_row.append(prev_row[i] + prev_row[i+1])
        current_row.append(1)

        return current_row