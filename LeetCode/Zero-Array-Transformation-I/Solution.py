class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        dif = [0] * (n+1) # diffeernece array of N+1
        for l, r in queries:
            dif[l] += 1
            dif[r+1] -= 1

        # making prefixsum 
        prefix = [dif[0]]
        for i in range(1,n+1):
            prefix.append(prefix[-1] + dif[i])

        # iterate on the prefix 0 , n-1
        for i in range(n):
            if nums[i] > prefix[i]:
                return False
        return True