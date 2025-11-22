# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

t = int(input())
for _ in range(t):
    l, r, d = map(int, input().split())
    if d < l:
        print(d)
    else:
        print((r // d + 1) * d)
        