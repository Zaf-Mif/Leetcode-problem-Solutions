# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def isValid(valid):
            car = 0
            for r in ranks:
                car += isqrt(valid // r)
            
            return car >= cars

        low = 1
        high = min(ranks) * (cars**2)

        while low <= high:
            mid = low + (high - low ) // 2

            if isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans