# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import defaultdict
t  = int(input())
sm = 0
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    dic = defaultdict(int)
    freq = defaultdict(int)
    
    for i in a:
        dic[i] += 1
        freq[dic[i]] += 1
    mx = 0
    for key,value in freq.items():
        mx = max(mx,(key*value))
    print(n - mx)