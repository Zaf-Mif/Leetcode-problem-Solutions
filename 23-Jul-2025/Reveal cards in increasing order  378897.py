# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [0] *n
        skip = False
        indeck = inresult = 0
        deck.sort()
        
        while indeck < n :
            if result[inresult] == 0:
                if not skip :
                    result[inresult] = deck[indeck]
                    indeck += 1
                skip = not skip
            inresult = (inresult + 1) %  n

        return result