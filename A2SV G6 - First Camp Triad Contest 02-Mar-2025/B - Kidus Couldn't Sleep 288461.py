# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n , k = map(int,input().split())
a = list(map(int,input().split()))
temp = n -k + 1
sub = sum (a[:k])
sm = sub
for i in range(k , n):
    sub += a[i] - a[i-k]
    sm += sub
print(sm / temp)