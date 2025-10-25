# Problem: Team Composition: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

import sys

input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
ans = []
idx = 1
for _ in range(t):
    a = int(input_data[idx]); b = int(input_data[idx+1]); idx += 2
    ans.append(str(min(min(a, b), (a + b) // 4)))
print("\n".join(ans))