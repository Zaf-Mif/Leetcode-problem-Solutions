class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # nums.sort()
        s1 ,s2 , s3 = nums[0] , nums[1] , nums[2]
        if (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2) :
            setx =  len(set(nums))
            if setx == 3:
                return "scalene"
            elif setx == 2: 
                return "isosceles"
            else: 
                return "equilateral"
        else:
            return "none"

