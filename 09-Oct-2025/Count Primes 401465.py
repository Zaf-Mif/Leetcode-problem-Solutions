# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        isPrime = [True for _ in range(n)]
        isPrime[0] = isPrime[1] = False
        i = 2
        while i*i < n:
            if isPrime[i]:
                j = i * i
                while j < n:
                    isPrime[j] = False
                    j += i
            i += 1
            
        cnt = 0
        for i in range(n):
            if isPrime[i]:
                cnt += 1
        return cnt