# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

n , m = map(int,input().split())
prefix = []
for i in range(n):
    c , t = map(int,input().split())
    
    prefix.append(c * t)
    if i > 0:
        prefix[i] += prefix[i-1]
        
moments = list(map(int,input().split()))

i = 0
for j in range(m):
    while moments[j] > prefix[i]:
        i += 1
        
    print(i + 1)