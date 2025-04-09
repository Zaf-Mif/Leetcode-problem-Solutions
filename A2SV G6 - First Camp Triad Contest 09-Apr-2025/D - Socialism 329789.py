# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

def check(nums):
    nums.sort(reverse = True)
    sm = 0
    for i in range(len(nums)):
        sm += nums[i]
        if sm / (i + 1) < x:
            return (i)
        
    return(n)
    
for _ in range(int(input())):
    n, x = map(int, input().split())
    
    nums = list(map(int, input().split()))
    print(check(nums))
 