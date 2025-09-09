# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []

        def dfs(curr: str, opened: int, balance: int) -> None:
            if len(curr) == 2 * n:
                res.append(curr)
                return
            if opened < n:
                dfs(curr + "(", opened + 1, balance + 1)
            if balance > 0:
                dfs(curr + ")", opened, balance - 1)

        dfs("", 0, 0)
        return res