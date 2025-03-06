# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # let we use mono decreasing stack
        mono_decreasing_stack = []
        ans = [0] * len(temperatures)
        for key , value in enumerate(temperatures):
            while mono_decreasing_stack and mono_decreasing_stack[-1][1] < value:
                val = key - mono_decreasing_stack[-1][0] 
                ans[mono_decreasing_stack[-1][0]] = val
                mono_decreasing_stack.pop()
            mono_decreasing_stack.append([key,value])
        return ans


