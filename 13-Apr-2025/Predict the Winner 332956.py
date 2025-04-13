# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0:
            return True  
        
        player = [[0] * n for _ in range(n)]
        
        for i in range(n):
            player[i][i] = nums[i]
        
        for length in range(2, n + 1):  
            for i in range(n - length + 1):
                j = i + length - 1
                player[i][j] = max(nums[i] - player[i + 1][j], nums[j] - player[i][j - 1])

        return player[0][n - 1] >= 0