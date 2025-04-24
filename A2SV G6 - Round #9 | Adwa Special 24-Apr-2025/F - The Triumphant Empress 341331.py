# Problem: F - The Triumphant Empress - https://codeforces.com/gym/601269/problem/F

n , m , k = map(int,input().split())
low = 1
high = n * m
while low <= high:
    mid = low + (high - low)  // 2
    
    # find elemnts 
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i , m)
    
    if cnt >= k:
        high = mid  - 1
    else:
        low = mid + 1
 
print(low) 