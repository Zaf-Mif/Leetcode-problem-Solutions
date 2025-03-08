# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        subdict = defaultdict(int)

        for c in blocks[:k]:
            subdict[c] += 1

        min_white = subdict["W"]

        for i in range(k , len(blocks)):

            subdict[blocks[i-k]]  -= 1
            if subdict[blocks[i-k]] == 0:
                del subdict[blocks[i-k]]

            subdict[blocks[i]] += 1
            
            min_white = min(min_white , subdict["W"])

        return min_white

            

