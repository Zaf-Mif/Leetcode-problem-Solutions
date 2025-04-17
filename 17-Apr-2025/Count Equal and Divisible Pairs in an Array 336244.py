# Problem: Count Equal and Divisible Pairs in an Array - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # by using counting sort 
        mx = max(nums)
        checker =[[] for _ in range(mx + 1)]

        for idx , value in enumerate(nums):
            checker[value].append(idx)
        
        count = 0
        for value in range(1, mx + 1):
            for i in range(len(checker[value])):
                for j in range(i + 1, len(checker[value])):
                    if (checker[value][i] * checker[value][j]) % k == 0:
                        count += 1
        
        return count