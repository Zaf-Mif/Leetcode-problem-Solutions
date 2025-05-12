# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        sm = 0
        pre = defaultdict(int)
        pre[0] = 1  
        for num in nums:
            sm += num
            cnt += pre[sm - k]
            pre[sm] += 1

        return cnt