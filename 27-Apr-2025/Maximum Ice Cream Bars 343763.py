# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        sm = 0
        for i in range(len(costs)):
            if sm + costs[i] <= coins:
                sm += costs[i]
                cnt += 1
        return cnt 