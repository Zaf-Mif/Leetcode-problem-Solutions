# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # time complexity = O(n*log(m))
        # space complexity = O(1)
        low = max(weights)# O(n)
        high = sum(weights)#O(n)
        ans = high

        while low <= high: # O(log(m(sum of arrays))) * O(n) 
            mid = low + (high - low) // 2
            day = 1
            store = 0

            for i in range(len(weights)):#O(n)
                if store + weights[i] <= mid:
                    store += weights[i]
                else:
                    store = weights[i]
                    day += 1

            if day <= days:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1
        
        return ans
        
                