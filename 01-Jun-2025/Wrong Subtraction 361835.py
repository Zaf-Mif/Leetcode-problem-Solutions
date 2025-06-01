# Problem: Wrong Subtraction - https://codeforces.com/problemset/problem/977/A?mobile=false

n,k=list(map(int,input().split()))
for i in range(k):
    if n%10!=0:
        n-=1
    else:
        n=int(n/10)
print(n)        