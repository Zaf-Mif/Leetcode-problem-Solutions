# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        mn=max(0,n-(2*limit))
        mx=limit
        ans=0

        for i in range(mn,mx+1):
            lower=max(n-i-limit,0)
            upper=min(limit,n-i)

            ans+=max(upper-lower+1,0)

        return ans



        