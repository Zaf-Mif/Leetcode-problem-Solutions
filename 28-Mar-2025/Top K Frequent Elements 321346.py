# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1 )]

        for key , value in cnt.items():
            bucket[value].append(key)

        res = []
        for i in range(len(bucket)-1 , -1 , -1):
            current = bucket[i]

            for num in current:
                res.append(num)

                if len(res) == k:
                    return res

