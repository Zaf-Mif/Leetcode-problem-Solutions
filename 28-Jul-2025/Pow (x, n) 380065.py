# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution: def myPow(self, x: float, n: int) -> float: self.cnt = 1 if n == 0: return 1 if n < 0: x = 1 / x n = -n def answer(num, nn): if nn == 0: return 1 half = answer(num , nn // 2) if nn % 2 == 0: return half * half else: return half * half * num return answer(x,n) 