# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = blocks[:k].count("W")
        min_white = white

        for i in range(k , len(blocks)):
            if blocks[i-k] == "W":
                white -= 1

            if blocks[i] == "W":
                white += 1
            
            min_white = min(min_white , white)

        return min_white

            
