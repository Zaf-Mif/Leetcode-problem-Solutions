# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())
for _ in range(t):
    n , m = map(int,input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    def inbound(row,col):
        return row >= 0 and row < n and col >= 0 and col < m
    mx = 0
    for row in range(n):
        for col in range(m):
            take = 0
            r , c = row , col
            while(inbound(r,c)):
                take += mat[r][c]
                r -= 1
                c -= 1
                
            r , c = row , col
            while(inbound(r,c)):
                take += mat[r][c]
                r += 1
                c -= 1
            
            r , c = row , col
            while(inbound(r,c)):
                take += mat[r][c]
                r -= 1
                c += 1
                
            r , c = row , col
            while(inbound(r,c)):
                take += mat[r][c]
                r += 1
                c += 1
            
            take -= (mat[row][col] * 3)
            mx = max(mx , take)
    print(mx)
        