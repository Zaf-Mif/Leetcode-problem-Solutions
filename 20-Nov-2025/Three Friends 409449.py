# Problem: Three Friends - https://codeforces.com/gym/451300/problem/C

x = list(map(int,input().split()))
# to find the minimum distance they can meet 
x.sort()
mid = x[1]
res = 0 
for i in range(3):
    res += abs(x[i]-mid)
print(res)