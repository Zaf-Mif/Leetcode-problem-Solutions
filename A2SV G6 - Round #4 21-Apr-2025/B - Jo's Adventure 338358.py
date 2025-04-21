# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n,m = map(int, input().split())
arr = list(map(int, input().split()))
pre = [0] * n 
suf = [0] * n

for i in range(1, n):
    pre[i] = pre[i - 1] + max(0, arr[i - 1] - arr[i])
    
for i in range(n-2,-1,-1):
    suf[i] = suf[i+1] + max (0 , arr[i+1]- arr[i])
    
for i in range(m):
    s , t = map(int, input().split())
    
    if t > s:
        print(pre[t-1] - pre[s-1])
    else:
        print(suf[t-1] - suf[s-1])