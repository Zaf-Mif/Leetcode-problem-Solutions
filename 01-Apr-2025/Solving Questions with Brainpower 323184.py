# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        cache = [0] * n

        for i in reversed(range(n)):
            points , brainpower = questions[i]
            nx = i + brainpower + 1

            choose = points + (cache[nx]if nx < n else 0)
            skip = cache[i+1]if i + 1 < n else 0

            cache[i] = max(choose , skip)

        return cache[0]