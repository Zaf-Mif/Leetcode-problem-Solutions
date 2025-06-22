# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def check(left, right):
            if left == right:
                return nums[left]

            pleft = nums[left] - check(left + 1, right)
            pright = nums[right] - check(left, right - 1)

            return max(pleft, pright)

        final = check(0, len(nums) - 1)
        return final >= 0