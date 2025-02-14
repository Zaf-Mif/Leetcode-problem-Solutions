# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ROWS =len(accounts)
        COLS = len(accounts[0])
        mx = 0
        for row in range(ROWS):
            sm = 0
            for col in range(COLS):
                sm += accounts[row][col]

            mx = max(mx, sm)

        return mx

        