# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        def check(i):
            target = nums[i]
            left, right, best = 0, i, i

            while left <= right:
                mid = (left + right) // 2
                cnt = i - mid + 1
                final = cnt * target
                original = prefix[i] - prefix[mid] + nums[mid]
                opr = final - original

                if opr > k:
                    left = mid + 1
                else:
                    best = mid 
                    right = mid - 1

            return i - best + 1
        
        nums.sort()
        prefix = [nums[0]]

        for num in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[num]) 

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, check(i))
        return ans

