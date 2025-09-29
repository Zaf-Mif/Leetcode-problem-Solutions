# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        same = cnt = oddmx = temp = 0
        for value in count.values():
            if value %2 == 0:
                cnt  += value
            if value % 2 != 0:
                if oddmx < value:
                    oddmx = value
        #  how many items are there as the length of the oddmx
        for value in count.values():
            if value == oddmx:
                same += 1
        if same > 1:
            temp += ((same-1)* (oddmx-1))
        for value in count.values():
            if value% 2 != 0:
                if  value != oddmx:
                    temp += (value-1)
        cnt += (oddmx + temp)
        return cnt 