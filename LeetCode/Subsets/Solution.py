class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        m = 2 ** n
        ans = []
        
        for num in range(m):
            temp = []
            i = 0 
            while num > 0 :
                if num & 1:
                    temp.append(nums[i])
                num >>= 1
                i += 1

            ans.append(temp)

        return ans
