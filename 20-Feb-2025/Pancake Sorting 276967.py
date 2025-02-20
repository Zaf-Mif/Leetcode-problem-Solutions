# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        nums = sorted(arr , reverse = True)
        res =[]
        for i in range(len(arr)):
            index = arr.index(nums[i])
            res.append(index+1)
            res.append(len(arr)-i)
            arr[:index+1] = arr[:index+1][::-1]
            arr[:len(arr)-i] = arr[:len(arr)-i][::-1]
        return res