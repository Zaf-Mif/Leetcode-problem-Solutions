# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        row, col = click

        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        def dfs(i: int, j: int):
            mine_cnt = 0
            for dx, dy in direction:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                    mine_cnt += 1

            if mine_cnt > 0:
                board[i][j] = str(mine_cnt)
                return

            board[i][j] = 'B'
            for dx, dy in direction:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'E':
                    dfs(ni, nj)

        dfs(row, col)
        return board

