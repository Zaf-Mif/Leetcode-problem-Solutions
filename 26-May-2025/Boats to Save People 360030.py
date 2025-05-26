# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left , right = 0 , len(people) -1
        result = 0

        while left <= right:
            remain = limit - people[right]
            right -= 1
            result += 1
            
            if remain >= people[left]:
                left += 1
        
        return result