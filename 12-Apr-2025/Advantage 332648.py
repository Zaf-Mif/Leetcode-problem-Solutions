# Problem: Advantage - https://codeforces.com/gym/452236/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    mx1 = max(arr)
    lst = sorted(arr)
    ans = [0]*n
    for i in range(n):
        if arr[i] == mx1:
            ans[i] = arr[i] - lst[-2]
        else:
            ans[i] = arr[i] - lst[-1]
    print(*ans)