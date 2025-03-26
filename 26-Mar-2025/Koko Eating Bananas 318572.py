# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(valid):
            k = 0
            rem = 0
            for i in piles:
                k += ((i // valid))  
                if i % valid != 0:
                    k += 1
     
            return k <= h

        high = max(piles)
        low = 1

        while low <= high:
            mid = low + (high - low) // 2

            if isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans

