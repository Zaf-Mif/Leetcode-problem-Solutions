# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

def canBe(s , w):
    target = sum(ord(c) for c in w)
    current = sum(ord(s[i]) for i in range(m))
    
    if target == current:
        return "YES"
    
    for i in range(m , n):
        current  += ord(s[i]) - ord(s[i-m])
        if target == current:
            return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n , m = map(int,input().split())
    s = input() # it has a lenght of n
    w = input() # it has a lenght of m
    print(canBe(s, w))