# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        res = []
        for i in nums:
            hashmap[i] += 1
        print(hashmap)
        for key,value in hashmap.items():
            if value > ((len(nums))//3):
                res.append(key)
        return res