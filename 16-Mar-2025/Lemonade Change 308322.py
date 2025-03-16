# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cent5 = 0
        cent10 = 0

        for i in bills:
            if i == 5:
                cent5 += 1
            elif i == 10 :
                cent10 += 1
                cent5 -= 1
            else:
                if cent10 > 0:
                    cent10 -= 1
                    cent5 -= 1

                else:
                    cent5 -= 3

            if cent5 < 0 :
                return False
        return True
            
