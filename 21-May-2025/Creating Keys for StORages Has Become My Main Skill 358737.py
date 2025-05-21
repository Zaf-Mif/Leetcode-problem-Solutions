# Problem: Creating Keys for StORages Has Become My Main Skill - https://codeforces.com/contest/2072/problem/C

t = int(input())
for _ in range(t):
    n , x = map(int,input().split())
    ans= [x]*n
    val = 0
    flag = True
    for i in range(n-1):
        if ((val | i ) & x) == (val |i):
            val |= i
            ans[i] = i
        else:
            flag = False
            break
        
    if flag and ((val|n-1) == x):
        ans[n-1] = n-1
    print(*ans)
        