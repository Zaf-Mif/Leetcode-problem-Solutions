# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        isPrime = [1 for _ in range(n)]
        isPrime[0] = isPrime[1] = 0
        for i in range(2, int(sqrt(n)) + 1):
            if isPrime[i]:
                for j in range(i*i, n,i):
                    isPrime[j] = 0
        cnt = 0
        for i in range(n):
            if isPrime[i]:
                cnt += 1
        return cnt