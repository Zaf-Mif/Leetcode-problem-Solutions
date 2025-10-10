# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        #  bruteforce
        n = len(nums)
        cnt = 0
        for i in range(n):
            cgcd = 0
            for j in range(i, n):
                cgcd =  gcd(nums[j], cgcd)

                if cgcd < k:
                    break
                
                if cgcd == k:
                    cnt += 1

        return cnt 
