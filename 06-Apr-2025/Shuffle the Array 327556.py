# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(len(nums) // 2):
            ans.append(nums[i])
            ans.append(nums[(len(nums)// 2) + i ])
        return ans