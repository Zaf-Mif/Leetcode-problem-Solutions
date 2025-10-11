# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

from math import gcd
n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
arr = []
g = 0
for i in range(1, n):
    g = gcd(g, a[i]-a[0])

for j in range(m):
    ans = gcd(a[0]+b[j], g)
    arr.append(ans)
print(*arr)

