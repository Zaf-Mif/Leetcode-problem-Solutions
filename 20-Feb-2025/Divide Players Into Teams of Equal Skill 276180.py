# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = sum(skill) // (len(skill) // 2 )
        print(ans)
        skill.sort()
        sm = 0
        left = 0
        right = len(skill) -1
        while left < right:
            if skill[left] + skill[right] != skill[left+1] +skill[right - 1]:
                return -1
            else:
                a = skill[left] *skill[right]
                sm += a
            left += 1
            right -= 1
        return sm