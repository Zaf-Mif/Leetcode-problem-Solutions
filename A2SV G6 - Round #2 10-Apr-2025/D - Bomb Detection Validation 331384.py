# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

def check(mat):
    # to count the bombs
    def count(x , y):
        bomb = 0
        for dx , dy in directions:
            nx , ny = x + dx , y + dy
            if inBound(nx , ny) and mat[nx][ny] == "*":
                bomb += 1
        return bomb
    
    valid = True
    # all the neighbours
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # check if it's inbound
    def inBound(row , col):
        return  0 <= row < n and 0 <= col < m
            
    for row in range(n):
        for col in range(m):
            
            if mat[row][col] == "*" :
                continue
            
            #  we have to count the number of bombs in it's neighbour
            bomb = count(row , col)
            
            if mat[row][col] == ".":
                if bomb > 0:
                    valid = False
                    
            else:
                if int(mat[row][col]) != bomb:
                    valid = False
                    
    return "YES" if valid else "NO"

n ,m  = map(int,input().split())
mat = []
for i in range(n):
    k = list(input())
    mat.append(k)
print(check(mat))