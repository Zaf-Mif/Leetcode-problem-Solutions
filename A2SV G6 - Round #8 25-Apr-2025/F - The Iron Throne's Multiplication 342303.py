# Problem: F - The Iron Throne's Multiplication - https://codeforces.com/gym/599383/problem/F

n , m , k = map(int,input().split())
low = 1
high = n * m
ans = None
 
while low <= high:
    mid = low + (high - low)  // 2
    
    #count number of elemnts
    '''
    for each row mid / i and assigning the minimum of mid/i and the len(col) that's m
    '''
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i , m)
    
    if cnt >= k:
        ans = mid
        high = mid  - 1
    else:
        low = mid + 1
 
print(ans)   