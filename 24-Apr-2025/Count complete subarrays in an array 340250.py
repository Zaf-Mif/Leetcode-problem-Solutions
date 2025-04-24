# Problem: Count complete subarrays in an array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        m = len(set(nums))
        n = len(nums)
        cnt = 0
        left = 0

        freq = defaultdict(int)
        for right in range(n):
            freq[nums[right]] += 1

            while len(freq) == m:
                cnt += (n - right)

                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                
                left += 1
        return cnt


