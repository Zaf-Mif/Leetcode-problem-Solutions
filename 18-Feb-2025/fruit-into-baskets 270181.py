# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit = defaultdict(int)
        left = right = mx = 0

        while right < len(fruits):
            fruit[fruits[right]] += 1
            
            while len(fruit) > 2:
                fruit[fruits[left]] -= 1
                
                if fruit[fruits[left]] == 0:
                    del fruit[fruits[left]]
                left += 1

            mx = max(mx , right-left+1)
            right += 1
        return mx