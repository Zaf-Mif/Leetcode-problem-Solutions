# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def count_almost_primes(n):
    count = 0
    for i in range(1, n + 1):
        prime_divisors = set()
        for j in range(2, i + 1):
            if i % j == 0 and is_prime(j):
                prime_divisors.add(j)
        if len(prime_divisors) == 2:
            count += 1
    return count

n = int(input())
cnt = 0 
print(count_almost_primes(n))