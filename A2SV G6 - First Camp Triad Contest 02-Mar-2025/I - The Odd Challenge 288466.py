# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())
for i in range(t):
    n , q = map(int,input().split())
    a = list(map(int,input().split()))
    ans = [0]
    for k in range(n):
        ans.append(ans[-1] + a[k])
    for j in range(q):
        l ,r , k = map(int,input().split())
        res = ((ans[-1] - ans[r] ) + ans[l-1] ) + ((r-l+1)*k)
        # print(ans , res)
        if res % 2 == 0:
            print("NO")
        else:
            print("YES")