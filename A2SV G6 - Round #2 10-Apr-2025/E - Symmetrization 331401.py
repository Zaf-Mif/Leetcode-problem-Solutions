# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t = int(input())
for _ in range(t):
    n = int(input())   
    mat = []
    for i in range(n):
        mat.append(input())
    
    mn = 0
    
    for row in range(n//2):
        
        for col in range(row, n - row - 1):
            zero = [0 , 0]
            zero[int(mat[row][col])] += 1
            zero[int(mat[col][n - row - 1])] += 1
            zero[int(mat[n - row - 1][n - col - 1])] += 1
            zero[int(mat[n - col - 1][row])] += 1
            
            mn += min (zero)
    
    print(mn)

            