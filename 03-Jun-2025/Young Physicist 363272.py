# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

n=int(input())
a=[]
sum=0
for i in range(n):
    x,y,z=list(map(int,input().split()))
    a.append(x)
for i in a:
    sum+=i
if sum==0:
    print("YES")
else:
    print("NO")