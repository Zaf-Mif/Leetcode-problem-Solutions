# Problem: Heaters  - https://leetcode.com/problems/heaters/

from typing import List
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        
        for house in houses:
            left , right = 0 , len(heaters)-1
            mn = float('inf')

            while left <= right:
                mid = (left + right) // 2
                mn = min(mn , abs(heaters[mid] - house))

                if heaters[mid] < house:
                    left = mid+ 1
                else:
                    right = mid -1

            res = max(res, mn)
        return res