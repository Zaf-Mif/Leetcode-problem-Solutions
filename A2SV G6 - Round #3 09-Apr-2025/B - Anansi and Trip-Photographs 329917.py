# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

def check(nums):
    nums.sort()
    front = nums[:n]
    back = nums[n:]
    
    # print(front , back)
    
    for i in range(n):
        if back[i] - front[i] < x:
            return "NO"
        
    return "YES"

t = int(input())
for i in range(t):
    n , x= list(map(int,input().split()))
    nums = list(map(int,input().split()))
    print(check(nums))