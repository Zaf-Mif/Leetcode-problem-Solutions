# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        freq = 0
        hash = defaultdict(int)
        for num in arr:
            idx = num % k
            comp = (k - idx) % k

            if comp in hash:  
                hash[comp] -= 1
                freq += 1
                if hash[comp] == 0:
                    del hash[comp]
            else:
                hash[idx] += 1
        print(freq)
        return freq == ((len(arr)) // 2)