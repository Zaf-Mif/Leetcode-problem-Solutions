# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

t = int(input())
for _ in range(t):
    n , s = map(int,input().split()) 
    index= ((n-1) - ((n-1) // 2 ) )+ 1
    ans = s // index 
    print(ans)
        
