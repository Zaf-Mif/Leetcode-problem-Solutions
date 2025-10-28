# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

n, m = map(int, input().split())

mn = (n + 1) // 2  
ans = -1

for x in range(mn, n + 1):
    if x % m == 0:
        ans = x
        break

print(ans)
