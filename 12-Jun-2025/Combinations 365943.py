# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(first_num):
            # handle basecases
            if len(path) == k:
                ans.append(path.copy())
                return 
                
            # iterate all possible candidates.
            for next_candidate in range(first_num + 1, n+1):

            # try this partial first_num solution
                path.append(next_candidate)

            # given the first_num, explore further.
                backtrack(next_candidate)

            # backtrack
                path.pop()
            
        path = []
        backtrack(0)
        return ans