# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        def custom(x):
            if int(x) == x:
                return int(x)
            else:
                return int(x) + 1

        cnt = Counter(answers)
        ans = 0
        for key , value in cnt.items():
            ans += custom(value / (key + 1)) * (key + 1)

        return ans