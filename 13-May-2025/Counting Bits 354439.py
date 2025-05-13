# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n+1):
            cnt = 0
            while num > 0:
                if num & 1 != 0:
                    cnt += 1
                num = num >> 1
            ans.append(cnt)
        return ans