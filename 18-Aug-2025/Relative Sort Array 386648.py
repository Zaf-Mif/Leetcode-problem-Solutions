# Problem: Relative Sort Array - https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash = defaultdict(int)
        for c in arr1:
            hash[c] += 1
        ans = []
        for i in arr2:
            val = hash[i]
            for _ in  range(val):
                ans.append(i)
                hash[i] -= 1
                if hash[i] == 0:
                    del hash[i]

        print(hash)
        #  sort hash 
        for h in sorted(hash.keys()):
            ans.extend([h] * hash[h])
        
        return ans
