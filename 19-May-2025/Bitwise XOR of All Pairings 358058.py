# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        Xor1 , Xor2 = 0 , 0 
        for num in nums1:
            Xor1 ^= num
        for num in nums2:
            Xor2 ^= num
            
        ans , res = 0, 0
        for i in range(len(nums1)):
            ans ^= Xor2
        for j in range(len(nums2)):
            res ^= Xor1

        return(res ^ ans)


