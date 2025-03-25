# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(valid):#O(n)
            day = 1
            store = 0
            for weight in weights:
                if store + weight <= valid:
                    store += weight
                else:
                    store = weight
                    day += 1
                    
            return day <= days

        low = max(weights)# O(n)
        high = sum(weights)#O(n)
        ans = high # O(1)

        while low <= high: # O(log(m(sum of arrays))) * O(n) 
            mid = low + (high - low) // 2

            if isValid(mid):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1
        
        # time complexity = O(n*log(m))
        # space complexity = O(1)
        return ans
        
                