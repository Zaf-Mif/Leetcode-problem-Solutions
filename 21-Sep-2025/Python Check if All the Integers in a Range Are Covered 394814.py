# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        myset=[]
        for member in ranges:
            for number in range(member[0],member[-1]+1):
                myset.append(number)
        testset=[]
        for num in range(left,right+1):
            testset.append(num)
        for test_number in testset:
            if test_number not in myset:
                return False
        return True