# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter,defaultdict
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    mx = 0
    set1 = set(s)
    a = len(s)//2
    if len(set1) == 1:
        print(2)
    else:
        cnt = Counter(s)
        se = defaultdict(int)
        for i in s:
            se[i] += 1
            
            cnt[i] -= 1
            if cnt[i] == 0:
                del cnt[i]
                
            cntS = len(cnt)
            cntJ = len(se)
            
            cn = cntS + cntJ
            mx = max(mx,cn)
        print(mx)