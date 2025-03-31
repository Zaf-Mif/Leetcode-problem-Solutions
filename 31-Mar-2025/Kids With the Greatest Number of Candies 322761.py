# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxCandy = max(candies)

        for candy in candies:
            ans.append(candy + extraCandies >= maxCandy)
        
        return ans
