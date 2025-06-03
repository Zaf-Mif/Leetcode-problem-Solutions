# Problem: Candy - https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        candies=[1]*n
        for i in range(n-1):
            if ratings[i+1]>ratings[i]:
                candies[i+1]=candies[i]+1
        for i in range(n-1):
            if ratings[n-1-(i+1)]>ratings[n-1-i] and candies[n-1-(i+1)]<=candies[n-1-i]:
                candies[n-1-(i+1)]=candies[n-1-i]+1
        print(candies)
        
        return sum(candies)