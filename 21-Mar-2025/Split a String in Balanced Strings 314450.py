# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        left ,  right = 0 , 0

        dic = defaultdict(int)
        dic[s[left]] += 1

        while right+1 < len(s):
            right += 1
            dic[s[right]] += 1


            if dic["R"] == dic["L"]:
                cnt += 1
                while left == right +1:
                    # left -= 1
                    dic[left] -= 1

                    if dic[left] == 0:
                        del dic[left]

                    left += 1

        return cnt 