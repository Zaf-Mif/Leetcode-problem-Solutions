# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        a= b = n // 2
        pr = sorted(costs, reverse = True, key = lambda x: abs(x[0]-x[1]))

        cnt = 0

        for pair in pr:
            city = pair.index(min(pair))
            if city == 0:
                if a > 0:
                    cnt += pair[0]
                    a -= 1
                else:
                    cnt += pair[1]
                    b -= 1
            else:
                if b > 0:
                    cnt += pair[1]
                    b -= 1
                else:
                    cnt += pair[0]
                    a -= 1
        
        return cnt