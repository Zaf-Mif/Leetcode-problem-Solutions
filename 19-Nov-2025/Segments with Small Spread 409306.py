# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

def check(n, k, a):
    mx = deque()  
    mn = deque()  
    
    left = 0
    ans = 0
    
    for right in range(n):
        while mx and mx[-1] < a[right]:
            mx.pop()
        mx.append(a[right])

        while mn and mn[-1] > a[right]:
            mn.pop()
        mn.append(a[right])

        while mx[0] - mn[0] > k:
            if a[left] == mx[0]:
                mx.popleft()
            if a[left] == mn[0]:
                mn.popleft()
            left += 1
        
        ans += (right - left + 1)
    
    return ans


n, k = map(int, input().split())
a = list(map(int, input().split()))
print(check(n, k, a))
