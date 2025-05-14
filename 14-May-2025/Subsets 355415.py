# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        m = 2 ** n
        ans = []
        
        for num in range(m):
            # it makes the "0b101" to 101 then it will fill them to leading 0 untill it length is n
            x = bin(num)[2:].zfill(n)
            # we have to find the binary of a and iterate through that bin 
            temp = []
            for i in range(n):
                if x[i] == "1":
                    temp.append(nums[i])

            ans.append(temp)

        return ans
