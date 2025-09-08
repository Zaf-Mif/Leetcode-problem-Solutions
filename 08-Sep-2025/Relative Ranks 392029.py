# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)
        sc = score.copy()
       
        sti = defaultdict(int)
        for i in range(N):
            sti[sc[i]] = i

        sc.sort(reverse = True)

        rank = [" "] * N
        for i in range(N):
            if i == 0: rank[sti[sc[i]]] = "Gold Medal"
            elif i == 1: rank[sti[sc[i]]] = "Silver Medal"
            elif i == 2: rank[sti[sc[i]]] = "Bronze Medal"
            else: rank[sti[sc[i]]] = str(i + 1)

        return rank