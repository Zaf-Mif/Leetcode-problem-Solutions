# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def isValid(valid):#O(n)
            day = 1
            store = 0
            for weight in nums:
                if store + weight <= valid:
                    store += weight
                else:
                    store = weight
                    day += 1
                    
            return day <= k

        low = max(nums)# O(n)
        high = sum(nums)#O(n)
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
        
                